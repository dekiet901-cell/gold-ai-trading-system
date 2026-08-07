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

    # =====================================================
    # TIME ZONES
    # =====================================================

    UTC = ZoneInfo("UTC")
    LONDON = ZoneInfo("Europe/London")
    NEW_YORK = ZoneInfo("America/New_York")

    # =====================================================
    # INTERNAL
    # =====================================================

    @staticmethod
    def _get_utc_now(now: datetime | None = None) -> datetime:
        """
        Return timezone-aware UTC datetime.
        """
        if now is None:
            return datetime.now(timezone.utc)

        if now.tzinfo is None:
            return now.replace(tzinfo=timezone.utc)

        return now.astimezone(timezone.utc)

    @staticmethod
    def _is_between(
        dt: datetime,
        start: time,
        end: time,
    ) -> bool:
        """
        Check if dt.time() is between start and end.
        """
        return start <= dt.time() < end

    # =====================================================
    # ASIA SESSION (UTC)
    # =====================================================

    @staticmethod
    def is_asia(now: datetime | None = None) -> bool:
        dt = Session._get_utc_now(now)
        return Session._is_between(
            dt,
            time(0, 0),
            time(9, 0),
        )

    # =====================================================
    # LONDON SESSION
    # =====================================================

    @staticmethod
    def is_london(now: datetime | None = None) -> bool:
        dt = Session._get_utc_now(now).astimezone(Session.LONDON)

        return Session._is_between(
            dt,
            time(8, 0),
            time(17, 0),
        )

    # =====================================================
    # NEW YORK SESSION
    # =====================================================

    @staticmethod
    def is_newyork(now: datetime | None = None) -> bool:
        dt = Session._get_utc_now(now).astimezone(Session.NEW_YORK)

        return Session._is_between(
            dt,
            time(8, 0),
            time(17, 0),
        )

    # =====================================================
    # NEW YORK AM
    # =====================================================

    @staticmethod
    def is_newyork_am(now: datetime | None = None) -> bool:
        dt = Session._get_utc_now(now).astimezone(Session.NEW_YORK)

        return Session._is_between(
            dt,
            time(8, 0),
            time(12, 0),
        )

    # =====================================================
    # NEW YORK LUNCH
    # =====================================================

    @staticmethod
    def is_newyork_lunch(now: datetime | None = None) -> bool:
        dt = Session._get_utc_now(now).astimezone(Session.NEW_YORK)

        return Session._is_between(
            dt,
            time(12, 0),
            time(13, 0),
        )

    # =====================================================
    # NEW YORK PM
    # =====================================================

    @staticmethod
    def is_newyork_pm(now: datetime | None = None) -> bool:
        dt = Session._get_utc_now(now).astimezone(Session.NEW_YORK)

        return Session._is_between(
            dt,
            time(13, 0),
            time(17, 0),
        )

    # =====================================================
    # ACTIVE SESSIONS
    # =====================================================

    @staticmethod
    def active_sessions(
        now: datetime | None = None,
    ) -> list[str]:

        sessions: list[str] = []

        if Session.is_asia(now):
            sessions.append("ASIA")

        if Session.is_london(now):
            sessions.append("LONDON")

        if Session.is_newyork(now):
            sessions.append("NEWYORK")

        return sessions if sessions else ["CLOSED"]

    # =====================================================
    # CURRENT SESSION
    # =====================================================

    @staticmethod
    def current(
        now: datetime | None = None,
    ) -> str:
        return " + ".join(Session.active_sessions(now))

    # =====================================================
    # CURRENT NEW YORK SUBSESSION
    # =====================================================

    @staticmethod
    def current_newyork(
        now: datetime | None = None,
    ) -> str:

        if Session.is_newyork_am(now):
            return "NY_AM"

        if Session.is_newyork_lunch(now):
            return "NY_LUNCH"

        if Session.is_newyork_pm(now):
            return "NY_PM"

        return "CLOSED"