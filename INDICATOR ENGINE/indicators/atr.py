"""
=========================================================
Gold AI Trading System
Average True Range (ATR)
=========================================================
"""

from __future__ import annotations

import pandas as pd

from CONFIG.indicator import IndicatorConfig


class ATR:
    """
    Average True Range Indicator.

    Dùng để:
    - đo volatility
    - tính SL/TP động
    - lọc sideway
    - quản lý breakout
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
        Validate OHLC dataframe.
        """

        if data.empty:
            raise ValueError(
                "DataFrame is empty."
            )

        required = [
            "high",
            "low",
            "close",
        ]

        for col in required:
            if col not in data.columns:
                raise KeyError(
                    f"Missing '{col}' column."
                )


    # =====================================================
    # TRUE RANGE
    # =====================================================

    @staticmethod
    def true_range(
        data: pd.DataFrame,
    ) -> pd.Series:
        """
        Calculate True Range.
        """

        previous_close = data["close"].shift(1)

        high_low = (
            data["high"]
            -
            data["low"]
        )

        high_close = (
            data["high"]
            -
            previous_close
        ).abs()

        low_close = (
            data["low"]
            -
            previous_close
        ).abs()


        tr = pd.concat(
            [
                high_low,
                high_close,
                low_close,
            ],
            axis=1,
        ).max(axis=1)


        return tr



    # =====================================================
    # ATR CALCULATION
    # =====================================================

    @staticmethod
    def calculate(
        data: pd.DataFrame,
        period: int,
    ) -> pd.Series:
        """
        Calculate ATR using EMA smoothing.
        """

        tr = ATR.true_range(data)


        atr = (
            tr
            .ewm(
                span=period,
                adjust=False,
            )
            .mean()
        )


        return atr



    # =====================================================
    # DEFAULT ATR
    # =====================================================

    def value(
        self,
        data: pd.DataFrame,
    ) -> pd.Series:
        """
        Calculate default ATR.
        """

        self._validate(data)


        return self.calculate(
            data,
            self.config.ATR_PERIOD,
        )



    # =====================================================
    # APPLY
    # =====================================================

    def apply(
        self,
        data: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Append ATR column.
        """

        self._validate(data)


        df = data.copy()


        df["atr"] = self.value(df)


        return df
