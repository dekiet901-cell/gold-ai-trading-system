"""
=========================================================
Gold AI Trading System
Core Engine Package
=========================================================
"""

from .cache import Cache, cache
from .data import Candle, Tick, DataEngine, data_engine
from .event import EventBus, event_bus
from .logger import Logger
from .market import MarketSnapshot, MarketEngine, market
from .memory import Memory, memory
from .mt5 import MT5Engine, mt5_engine
from .realtime import RealtimeEngine, realtime
from .scheduler import Scheduler, scheduler
from .timeframe import (
    Timeframe,
    TIMEFRAME_SECONDS,
    get_seconds,
    from_string,
    to_string,
    is_valid,
)
from .utils import (
    now,
    timestamp,
    ensure_directory,
    file_exists,
    load_json,
    save_json,
    clamp,
    round_price,
    is_empty,
    safe_float,
    safe_int,
    to_dict,
)

__all__ = [
    "Cache",
    "cache",

    "Candle",
    "Tick",
    "DataEngine",
    "data_engine",

    "EventBus",
    "event_bus",

    "Logger",

    "MarketSnapshot",
    "MarketEngine",
    "market",

    "Memory",
    "memory",

    "MT5Engine",
    "mt5_engine",

    "RealtimeEngine",
    "realtime",

    "Scheduler",
    "scheduler",

    "Timeframe",
    "TIMEFRAME_SECONDS",
    "get_seconds",
    "from_string",
    "to_string",
    "is_valid",

    "now",
    "timestamp",
    "ensure_directory",
    "file_exists",
    "load_json",
    "save_json",
    "clamp",
    "round_price",
    "is_empty",
    "safe_float",
    "safe_int",
    "to_dict",
]
