"""
=========================================================
Gold AI Trading System
Bollinger Bands
=========================================================
"""

from __future__ import annotations

import pandas as pd

from CONFIG.indicator import IndicatorConfig


class Bollinger:
    """
    Bollinger Bands Indicator.
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

        if data.empty:
            raise ValueError("DataFrame is empty.")

        if "close" not in data.columns:
            raise KeyError("Missing 'close' column.")

    # =====================================================
    # CALCULATION
    # =====================================================

    @staticmethod
    def calculate(
        series: pd.Series,
        period: int,
        deviation: float,
    ) -> tuple[pd.Series, pd.Series, pd.Series]:

        middle = series.rolling(period).mean()

        std = series.rolling(period).std()

        upper = middle + deviation * std

        lower = middle - deviation * std

        return upper, middle, lower

    # =====================================================
    # APPLY
    # =====================================================

    def apply(
        self,
        data: pd.DataFrame,
    ) -> pd.DataFrame:

        self._validate(data)

        df = data.copy()

        upper, middle, lower = self.calculate(
            df["close"],
            self.config.BB_PERIOD,
            self.config.BB_DEVIATION,
        )

        df["bb_upper"] = upper
        df["bb_middle"] = middle
        df["bb_lower"] = lower

        return df

    # =====================================================
    # SIGNAL
    # =====================================================

    @staticmethod
    def signal(
        data: pd.DataFrame,
    ) -> pd.Series:

        signal = pd.Series(
            "NEUTRAL",
            index=data.index,
        )

        signal.loc[
            data["close"] > data["bb_upper"]
        ] = "OVERBOUGHT"

        signal.loc[
            data["close"] < data["bb_lower"]
        ] = "OVERSOLD"

        return signal
