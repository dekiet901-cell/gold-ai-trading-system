"""
=========================================================
Gold AI Trading System
Relative Strength Index (RSI)
=========================================================
"""

from __future__ import annotations

import pandas as pd

from CONFIG.indicator import IndicatorConfig


class RSI:
    """
    Relative Strength Index Indicator.
    """

    def __init__(
        self,
        config: IndicatorConfig | None = None,
    ) -> None:

        self.config = config or IndicatorConfig()


    # =====================================================
    # VALIDATION
    # =====================================================

    @staticmethod
    def _validate(
        data: pd.DataFrame,
    ) -> None:
        """
        Validate input dataframe.
        """

        if data.empty:
            raise ValueError(
                "DataFrame is empty."
            )

        if "close" not in data.columns:
            raise KeyError(
                "Missing 'close' column."
            )


    # =====================================================
    # RSI CALCULATION
    # =====================================================

    @staticmethod
    def calculate(
        series: pd.Series,
        period: int,
    ) -> pd.Series:
        """
        Calculate RSI.
        """

        delta = series.diff()

        gain = delta.clip(
            lower=0
        )

        loss = -delta.clip(
            upper=0
        )


        avg_gain = gain.ewm(
            alpha=1 / period,
            adjust=False,
        ).mean()


        avg_loss = loss.ewm(
            alpha=1 / period,
            adjust=False,
        ).mean()


        rs = avg_gain / avg_loss


        rsi = 100 - (
            100 / (1 + rs)
        )


        return rsi


    # =====================================================
    # MAIN RSI
    # =====================================================

    def value(
        self,
        data: pd.DataFrame,
    ) -> pd.Series:
        """
        Return RSI value.
        """

        self._validate(data)

        return self.calculate(
            data["close"],
            self.config.RSI_PERIOD,
        )


    # =====================================================
    # SIGNAL
    # =====================================================

    def signal(
        self,
        data: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Append RSI and signal columns.
        """

        self._validate(data)

        df = data.copy()

        df["rsi"] = self.value(df)


        df["rsi_signal"] = "NEUTRAL"


        df.loc[
            df["rsi"] >= self.config.RSI_OVERBOUGHT,
            "rsi_signal"
        ] = "OVERBOUGHT"


        df.loc[
            df["rsi"] <= self.config.RSI_OVERSOLD,
            "rsi_signal"
        ] = "OVERSOLD"


        return df
