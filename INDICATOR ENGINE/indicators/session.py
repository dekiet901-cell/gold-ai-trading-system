"""
=========================================================
Gold AI Trading System
Trading Session Indicator
=========================================================
"""

from __future__ import annotations

from datetime import datetime, time, timezone
from zoneinfo import ZoneInfo


class Session:
    """
    Market trading session detector.
    """

    # Session hours (local time)
    ASIA_START = time(0, 0)
    ASIA_END = time(9, 0)

    LONDON_START = time(8, 0)
    LONDON_END = time(17, 0)

    NEWYORK_START = time(8, 0)
    NEWYORK_END = time(17, 0)

    @staticmethod
    def _get_utc_now(now: datetime | None = None) -> datetime:
        """
        Return a timezone-aware UTC datetime.
        """
        if now is None:
            return datetime.now(timezone.utc)

        if now.tzinfo is None:
            return now.replace(tzinfo=timezone.utc)

        return now.astimezone(timezone.utc)

    @staticmethod
    def is_asia(now: datetime | None = None) -> bool:
        dt = Session._get_utc_now(now)
        return Session.ASIA_START <= dt.time() < Session.ASIA_END

    @staticmethod
    def is_london(now: datetime | None = None) -> bool:
        dt = Session._get_utc_now(now).astimezone(
            ZoneInfo("Europe/London")
        )
        return Session.LONDON_START <= dt.time() < Session.LONDON_END

    @staticmethod
    def is_newyork(now: datetime | None = None) -> bool:
        dt = Session._get_utc_now(now).astimezone(
            ZoneInfo("America/New_York")
        )
        return Session.NEWYORK_START <= dt.time() < Session.NEWYORK_END

    @staticmethod
    def active_sessions(now: datetime | None = None) -> list[str]:
        sessions: list[str] = []

        if Session.is_asia(now):
            sessions.append("ASIA")

        if Session.is_london(now):
            sessions.append("LONDON")

        if Session.is_newyork(now):
            sessions.append("NEWYORK")

        return sessions if sessions else ["CLOSED"]

    @staticmethod
    def current(now: datetime | None = None) -> str:
        return " + ".join(Session.active_sessions(now))