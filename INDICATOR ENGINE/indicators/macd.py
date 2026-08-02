"""
=========================================================
Gold AI Trading System
MACD Indicator
=========================================================
"""

from __future__ import annotations

import pandas as pd

from CONFIG.indicator import IndicatorConfig


class MACD:
    """
    Moving Average Convergence Divergence.
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
        fast: int,
        slow: int,
        signal: int,
    ):

        ema_fast = series.ewm(
            span=fast,
            adjust=False,
        ).mean()

        ema_slow = series.ewm(
            span=slow,
            adjust=False,
        ).mean()

        macd = ema_fast - ema_slow

        signal_line = macd.ewm(
            span=signal,
            adjust=False,
        ).mean()

        histogram = macd - signal_line

        return (
            macd,
            signal_line,
            histogram,
        )

    # =====================================================
    # APPLY
    # =====================================================

    def apply(
        self,
        data: pd.DataFrame,
    ) -> pd.DataFrame:

        self._validate(data)

        df = data.copy()

        macd, signal, hist = self.calculate(
            df["close"],
            self.config.MACD_FAST,
            self.config.MACD_SLOW,
            self.config.MACD_SIGNAL,
        )

        df["macd"] = macd
        df["macd_signal"] = signal
        df["macd_hist"] = hist

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
            data["macd"] > data["macd_signal"]
        ] = "BUY"

        signal.loc[
            data["macd"] < data["macd_signal"]
        ] = "SELL"

        return signal
