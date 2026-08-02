"""
=========================================================
Gold AI Trading System
VWAP Indicator
=========================================================
"""

from __future__ import annotations

import pandas as pd

from CONFIG.indicator import IndicatorConfig


class VWAP:
    """
    Volume Weighted Average Price.
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

        required = [
            "high",
            "low",
            "close",
            "tick_volume",
        ]

        for column in required:

            if column not in data.columns:
                raise KeyError(
                    f"Missing '{column}' column."
                )

    # =====================================================
    # CALCULATION
    # =====================================================

    @staticmethod
    def calculate(
        data: pd.DataFrame,
    ) -> pd.Series:

        typical_price = (
            data["high"]
            + data["low"]
            + data["close"]
        ) / 3

        cumulative_tp_volume = (
            typical_price
            * data["tick_volume"]
        ).cumsum()

        cumulative_volume = (
            data["tick_volume"]
        ).cumsum()

        return (
            cumulative_tp_volume
            / cumulative_volume
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

        df["vwap"] = self.calculate(df)

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
            data["close"] > data["vwap"]
        ] = "BUY"

        signal.loc[
            data["close"] < data["vwap"]
        ] = "SELL"

        return signal
