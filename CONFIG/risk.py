"""
=========================================================
Gold AI Trading System
Risk Configuration
=========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RiskConfig:
    """
    Risk Management Configuration
    """

    # =====================================================
    # ACCOUNT
    # =====================================================

    ACCOUNT_RISK_PERCENT: float = 1.0

    MAX_DAILY_LOSS_PERCENT: float = 3.0

    MAX_DAILY_PROFIT_PERCENT: float = 10.0

    MAX_DRAWDOWN_PERCENT: float = 20.0

    # =====================================================
    # LOT
    # =====================================================

    FIXED_LOT: float = 0.01

    AUTO_LOT: bool = False

    MIN_LOT: float = 0.01

    MAX_LOT: float = 10.0

    # =====================================================
    # RISK / REWARD
    # =====================================================

    MIN_RR: float = 2.0

    DEFAULT_SL_POINTS: int = 300

    DEFAULT_TP_POINTS: int = 600

    # =====================================================
    # TRAILING STOP
    # =====================================================

    ENABLE_TRAILING: bool = True

    TRAILING_START: int = 300

    TRAILING_STEP: int = 100

    # =====================================================
    # BREAK EVEN
    # =====================================================

    ENABLE_BREAK_EVEN: bool = True

    BREAK_EVEN_TRIGGER: int = 250

    # =====================================================
    # PARTIAL TAKE PROFIT
    # =====================================================

    ENABLE_PARTIAL_CLOSE: bool = True

    PARTIAL_CLOSE_PERCENT: float = 50.0

    PARTIAL_CLOSE_TRIGGER: int = 200

    # =====================================================
    # POSITION
    # =====================================================

    MAX_OPEN_POSITIONS: int = 4

    MAX_TRADES_PER_DAY: int = 20