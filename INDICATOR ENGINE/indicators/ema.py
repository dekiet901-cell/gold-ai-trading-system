"""
=========================================================
Gold AI Trading System
Exponential Moving Average (EMA)
=========================================================
"""

from __future__ import annotations

import pandas as pd

from CONFIG.indicator import IndicatorConfig


class EMA:
    """
    Exponential Moving Average Indicator.
    """

    def __init__(self, config: IndicatorConfig | None = None) -> None:

        self.config = config or IndicatorConfig()

    # =====================================================
    # VALIDATION
    # =====================================================

    @staticmethod
    def _validate(data: pd.DataFrame) -> None:
        """
        Validate input dataframe.
        """

        if data.empty:
            raise ValueError("DataFrame is empty.")

        if "close" not in data.columns:
            raise KeyError("Missing 'close' column.")

    # =====================================================
    # EMA
    # =====================================================

    @staticmethod
    def calculate(
        series: pd.Series,
        period: int,
    ) -> pd.Series:
        """
        Calculate EMA.
        """

        return series.ewm(
            span=period,
            adjust=False,
        ).mean()

    # =====================================================
    # FAST
    # =====================================================

    def fast(
        self,
        data: pd.DataFrame,
    ) -> pd.Series:
        """
        Fast EMA.
        """

        self._validate(data)

        return self.calculate(
            data["close"],
            self.config.EMA_FAST,
        )

    # =====================================================
    # SLOW
    # =====================================================

    def slow(
        self,
        data: pd.DataFrame,
    ) -> pd.Series:
        """
        Slow EMA.
        """

        self._validate(data)

        return self.calculate(
            data["close"],
            self.config.EMA_SLOW,
        )

    # =====================================================
    # TREND
    # =====================================================

    def trend(
        self,
        data: pd.DataFrame,
    ) -> pd.Series:
        """
        Trend EMA.
        """

        self._validate(data)

        return self.calculate(
            data["close"],
            self.config.EMA_TREND,
        )

    # =====================================================
    # ALL
    # =====================================================

    def apply(
        self,
        data: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Append EMA columns.
        """

        self._validate(data)

        df = data.copy()

        df["ema_fast"] = self.fast(df)
        df["ema_slow"] = self.slow(df)
        df["ema_trend"] = self.trend(df)

        return df
