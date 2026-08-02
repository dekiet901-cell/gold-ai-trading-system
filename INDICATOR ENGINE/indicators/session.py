"""
=========================================================
Gold AI Trading System
Trading Session Indicator
=========================================================
"""

from __future__ import annotations

from datetime import datetime, time


class Session:
    """
    Market trading session detector.
    """

    # =====================================================
    # ASIA SESSION
    # =====================================================

    @staticmethod
    def asia(
        now: datetime | None = None,
    ) -> bool:

        now = now or datetime.utcnow()

        current = now.time()

        return (
            time(0, 0)
            <= current
            < time(8, 0)
        )

    # =====================================================
    # LONDON SESSION
    # =====================================================

    @staticmethod
    def london(
        now: datetime | None = None,
    ) -> bool:

        now = now or datetime.utcnow()

        current = now.time()

        return (
            time(8, 0)
            <= current
            < time(16, 0)
        )

    # =====================================================
    # NEW YORK SESSION
    # =====================================================

    @staticmethod
    def newyork(
        now: datetime | None = None,
    ) -> bool:

        now = now or datetime.utcnow()

        current = now.time()

        return (
            time(13, 0)
            <= current
            < time(21, 0)
        )

    # =====================================================
    # CURRENT SESSION
    # =====================================================

    @staticmethod
    def current(
        now: datetime | None = None,
    ) -> str:

        if Session.asia(now):
            return "ASIA"

        if Session.london(now):
            return "LONDON"

        if Session.newyork(now):
            return "NEWYORK"

        return "CLOSED"
