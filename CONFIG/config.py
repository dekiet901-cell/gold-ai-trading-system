"""
=========================================================
Gold AI Trading System
Global Configuration
=========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from .system import SystemConfig
from .mt5 import MT5Config
from .indicator import IndicatorConfig
from .risk import RiskConfig
from .telegram import TelegramConfig
from .ai import AIConfig



@dataclass(frozen=True)
class Config:
    """
    Global configuration container.
    """

    # =====================================================
    # SYSTEM
    # =====================================================

    SYSTEM: type[SystemConfig] = SystemConfig


    # =====================================================
    # MT5
    # =====================================================

    MT5: type[MT5Config] = MT5Config


    # =====================================================
    # INDICATORS
    # =====================================================

    INDICATOR: type[IndicatorConfig] = IndicatorConfig


    # =====================================================
    # RISK
    # =====================================================

    RISK: type[RiskConfig] = RiskConfig


    # =====================================================
    # TELEGRAM
    # =====================================================

    TELEGRAM: type[TelegramConfig] = TelegramConfig


    # =====================================================
    # AI
    # =====================================================

    AI: type[AIConfig] = AIConfig