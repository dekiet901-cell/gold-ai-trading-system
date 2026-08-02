"""
=========================================================
Gold AI Trading System
AI Configuration
=========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AIConfig:
    """
    Artificial Intelligence Configuration
    """

    # =====================================================
    # AI
    # =====================================================

    ENABLE: bool = True

    MODEL_NAME: str = "GoldAI"

    MODEL_VERSION: str = "1.0"

    # =====================================================
    # SCORING
    # =====================================================

    MIN_SCORE: int = 70

    MAX_SCORE: int = 100

    # =====================================================
    # WEIGHT
    # =====================================================

    TREND_WEIGHT: int = 25

    SMC_WEIGHT: int = 30

    INDICATOR_WEIGHT: int = 25

    VOLUME_WEIGHT: int = 10

    SESSION_WEIGHT: int = 10

    # =====================================================
    # FILTER
    # =====================================================

    REQUIRE_TREND: bool = True

    REQUIRE_SMC: bool = True

    REQUIRE_VOLUME: bool = False

    REQUIRE_SESSION: bool = False

    # =====================================================
    # HISTORY
    # =====================================================

    TRAINING_BARS: int = 500

    # =====================================================
    # CONFIDENCE
    # =====================================================

    MIN_CONFIDENCE: float = 0.75