"""
=========================================================
Gold AI Trading Assistant
Core Utility Engine
=========================================================
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

import json



# =====================================================
# TIME
# =====================================================

def now():

    return datetime.now()



def timestamp():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )



# =====================================================
# FILE
# =====================================================

def ensure_directory(
    path: str | Path
):

    directory = Path(path)

    directory.mkdir(
        parents=True,
        exist_ok=True
    )



def file_exists(
    path: str | Path
):

    return Path(path).exists()



def load_json(
    file_path: str | Path
):

    path = Path(file_path)


    if not path.exists():

        return {}


    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except Exception:

        return {}



def save_json(
    file_path: str | Path,
    data: dict
):

    path = Path(file_path)


    ensure_directory(
        path.parent
    )


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False,
            default=str
        )



# =====================================================
# NUMBER
# =====================================================

def clamp(
    value: float,
    minimum: float,
    maximum: float
):

    return max(
        minimum,
        min(value, maximum)
    )



def round_price(
    price: float,
    digits: int = 2
):

    return round(
        price,
        digits
    )



# =====================================================
# VALIDATE
# =====================================================

def is_empty(
    value
):

    return value is None or value == ""



def safe_float(
    value,
    default: float = 0.0
):

    try:

        return float(value)


    except Exception:

        return default



def safe_int(
    value,
    default: int = 0
):

    try:

        return int(value)


    except Exception:

        return default



# =====================================================
# CONVERT
# =====================================================

def to_dict(
    obj
):

    if hasattr(
        obj,
        "__dict__"
    ):

        return obj.__dict__


    return obj