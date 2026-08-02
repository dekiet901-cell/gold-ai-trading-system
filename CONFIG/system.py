"""
=========================================================
Gold AI Trading System
System Configuration
=========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path



@dataclass(frozen=True)
class SystemConfig:
    """
    Global system configuration.
    """



    # =====================================================
    # PROJECT
    # =====================================================

    PROJECT_NAME: str = "Gold AI Trading System"

    VERSION: str = "1.0.0"

    AUTHOR: str = "Gold AI"

    DEBUG: bool = True



    # =====================================================
    # ROOT DIRECTORY
    # =====================================================

    ROOT_DIR: Path = Path(__file__).resolve().parent.parent



    # =====================================================
    # FOLDERS
    # =====================================================

    APP_DIR: Path = ROOT_DIR / "APP"

    AI_DIR: Path = ROOT_DIR / "AI ENGINE"

    CONFIG_DIR: Path = ROOT_DIR / "CONFIG"

    CORE_DIR: Path = ROOT_DIR / "CORE ENGINE" / "core"

    DATABASE_DIR: Path = ROOT_DIR / "DATABASE"

    DASHBOARD_DIR: Path = ROOT_DIR / "DASHBOARD"

    EXECUTION_DIR: Path = ROOT_DIR / "EXECUTION ENGINE"

    INDICATORS_DIR: Path = ROOT_DIR / "INDICATOR ENGINE"

    LOGS_DIR: Path = ROOT_DIR / "LOGS"

    MODELS_DIR: Path = ROOT_DIR / "models"

    RISK_DIR: Path = ROOT_DIR / "RISK ENGINE"

    SMC_DIR: Path = ROOT_DIR / "SMC ENGINE"

    STRATEGY_DIR: Path = ROOT_DIR / "STRATEGY ENGINE"

    TELE_DIR: Path = ROOT_DIR / "TELEGRAM ENGINE"

    TREND_DIR: Path = ROOT_DIR / "TREND ENGINE"



    # =====================================================
    # DATABASE FILES
    # =====================================================

    MARKET_DB: Path = DATABASE_DIR / "market.db"

    TRADE_DB: Path = DATABASE_DIR / "trade.db"

    SIGNAL_DB: Path = DATABASE_DIR / "signal.db"

    LOG_DB: Path = DATABASE_DIR / "logs.db"



    # =====================================================
    # LOG FILES
    # =====================================================

    BOT_LOG: Path = LOGS_DIR / "bot.log"

    TRADE_LOG: Path = LOGS_DIR / "trade.log"

    ERROR_LOG: Path = LOGS_DIR / "error.log"



    # =====================================================
    # INITIALIZE PROJECT
    # =====================================================

    @classmethod
    def initialize(cls) -> None:
        """
        Create required folders.
        """

        folders = (

            cls.DATABASE_DIR,

            cls.LOGS_DIR,

            cls.MODELS_DIR,

        )


        for folder in folders:

            folder.mkdir(
                parents=True,
                exist_ok=True
            )