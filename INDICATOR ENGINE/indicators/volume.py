"""
=========================================================
Gold AI Trading System
Volume Indicator
=========================================================
"""

from __future__ import annotations

import pandas as pd

from CONFIG.indicator import IndicatorConfig


class Volume:
    """
    Volume Indicator.
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

        if "tick_volume" not in data.columns:
            raise KeyError("Missing 'tick_volume' column.")

    # =====================================================
    # CALCULATION
    # =====================================================

    @staticmethod
    def calculate(
        series: pd.Series,
        period: int,
    ) -> pd.Series:

        return series.rolling(
            window=period,
        ).mean()

    # =====================================================
    # APPLY
    # =====================================================

    def apply(
        self,
        data: pd.DataFrame,
    ) -> pd.DataFrame:

        self._validate(data)

        df = data.copy()

        df["volume_ma"] = self.calculate(
            df["tick_volume"],
            self.config.VOLUME_PERIOD,
        )

        return df

    # =====================================================
    # SIGNAL
    # =====================================================

    @staticmethod
    def signal(
        data: pd.DataFrame,
    ) -> pd.Series:

        signal = pd.Series(
            "NORMAL",
            index=data.index,
        )

        signal.loc[
            data["tick_volume"] > data["volume_ma"]
        ] = "HIGH"

        signal.loc[
            data["tick_volume"] < data["volume_ma"]
        ] = "LOW"

        return signal
