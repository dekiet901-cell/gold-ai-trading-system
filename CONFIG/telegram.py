"""
=========================================================
Gold AI Trading System
Telegram Configuration
=========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TelegramConfig:
    """
    Telegram Bot Configuration
    """

    # =====================================================
    # BOT
    # =====================================================

    ENABLE: bool = True

    BOT_TOKEN: str = ""

    CHAT_ID: str = ""

    # =====================================================
    # MESSAGE
    # =====================================================

    SEND_SIGNAL: bool = True

    SEND_ORDER: bool = True

    SEND_CLOSE: bool = True

    SEND_ERROR: bool = True

    SEND_STARTUP: bool = True

    SEND_SHUTDOWN: bool = True

    SEND_HEARTBEAT: bool = False

    # =====================================================
    # PHOTO
    # =====================================================

    SEND_CHART: bool = True

    # =====================================================
    # COMMAND
    # =====================================================

    ENABLE_COMMAND: bool = True

    # =====================================================
    # RETRY
    # =====================================================

    RETRY: int = 3

    RETRY_DELAY: int = 5

    # =====================================================
    # TIMEOUT
    # =====================================================

    TIMEOUT: int = 30