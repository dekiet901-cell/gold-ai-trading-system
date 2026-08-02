"""
=========================================================
Gold AI Trading System
SuperTrend Indicator
=========================================================
"""

from __future__ import annotations

import pandas as pd

from CONFIG.indicator import IndicatorConfig


class SuperTrend:
    """
    SuperTrend Indicator.
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
        ]

        for column in required:

            if column not in data.columns:
                raise KeyError(
                    f"Missing '{column}' column."
                )

    # =====================================================
    # ATR
    # =====================================================

    @staticmethod
    def _atr(
        data: pd.DataFrame,
        period: int,
    ) -> pd.Series:

        high = data["high"]
        low = data["low"]
        close = data["close"]

        tr = pd.concat(
            [
                high - low,
                (high - close.shift()).abs(),
                (low - close.shift()).abs(),
            ],
            axis=1,
        ).max(axis=1)

        return tr.rolling(
            period,
        ).mean()

    # =====================================================
    # CALCULATION
    # =====================================================

    def calculate(
        self,
        data: pd.DataFrame,
    ):

        atr = self._atr(
            data,
            self.config.SUPERTREND_PERIOD,
        )

        hl2 = (
            data["high"]
            + data["low"]
        ) / 2

        upperband = (
            hl2
            + self.config.SUPERTREND_MULTIPLIER * atr
        )

        lowerband = (
            hl2
            - self.config.SUPERTREND_MULTIPLIER * atr
        )

        final_upper = upperband.copy()
        final_lower = lowerband.copy()

        supertrend = pd.Series(
            index=data.index,
            dtype=float,
        )

        direction = pd.Series(
            True,
            index=data.index,
            dtype=bool,
        )

        for i in range(1, len(data)):

            if (
                upperband.iloc[i] < final_upper.iloc[i - 1]
                or data["close"].iloc[i - 1]
                > final_upper.iloc[i - 1]
            ):

                final_upper.iloc[i] = upperband.iloc[i]

            else:

                final_upper.iloc[i] = final_upper.iloc[i - 1]

            if (
                lowerband.iloc[i] > final_lower.iloc[i - 1]
                or data["close"].iloc[i - 1]
                < final_lower.iloc[i - 1]
            ):

                final_lower.iloc[i] = lowerband.iloc[i]

            else:

                final_lower.iloc[i] = final_lower.iloc[i - 1]

            if direction.iloc[i - 1]:

                direction.iloc[i] = (
                    data["close"].iloc[i]
                    > final_upper.iloc[i]
                )

            else:

                direction.iloc[i] = not (
                    data["close"].iloc[i]
                    < final_lower.iloc[i]
                )

            if direction.iloc[i]:

                supertrend.iloc[i] = final_lower.iloc[i]

            else:

                supertrend.iloc[i] = final_upper.iloc[i]

        return (
            supertrend,
            direction,
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

        supertrend, direction = self.calculate(df)

        df["supertrend"] = supertrend
        df["trend_up"] = direction

        return df

    # =====================================================
    # SIGNAL
    # =====================================================

    @staticmethod
    def signal(
        data: pd.DataFrame,
    ) -> pd.Series:

        signal = pd.Series(
            "SELL",
            index=data.index,
        )

        signal.loc[
            data["trend_up"]
        ] = "BUY"

        return signal
