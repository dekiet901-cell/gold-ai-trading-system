"""
=========================================================
Gold AI Trading Assistant
Core Timeframe Engine
=========================================================
"""

from __future__ import annotations

from enum import Enum



class Timeframe(Enum):
    """
    Trading timeframe definition
    """

    M1 = "M1"
    M5 = "M5"
    M15 = "M15"
    M30 = "M30"
    H1 = "H1"
    H4 = "H4"
    D1 = "D1"





# =====================================================
# TIMEFRAME MAP
# =====================================================

TIMEFRAME_SECONDS = {

    Timeframe.M1: 60,

    Timeframe.M5: 300,

    Timeframe.M15: 900,

    Timeframe.M30: 1800,

    Timeframe.H1: 3600,

    Timeframe.H4: 14400,

    Timeframe.D1: 86400,

}





# =====================================================
# GET SECONDS
# =====================================================

def get_seconds(
    timeframe: Timeframe
) -> int:

    return TIMEFRAME_SECONDS.get(
        timeframe,
        60
    )





# =====================================================
# STRING CONVERT
# =====================================================

def from_string(
    value: str
) -> Timeframe:

    value = value.upper()


    for tf in Timeframe:

        if tf.value == value:

            return tf


    raise ValueError(
        f"Invalid timeframe: {value}"
    )





def to_string(
    timeframe: Timeframe
) -> str:

    return timeframe.value





# =====================================================
# VALIDATE
# =====================================================

def is_valid(
    value: str
) -> bool:

    try:

        from_string(value)

        return True


    except ValueError:

        return False