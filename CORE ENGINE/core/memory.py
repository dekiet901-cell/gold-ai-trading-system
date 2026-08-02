"""
=========================================================
Gold AI Trading Assistant
Core Memory Engine
=========================================================
"""

from __future__ import annotations

from datetime import datetime
from copy import deepcopy





class Memory:



    def __init__(self):

        self.data = {}

        self.reset()





    # =====================================================
    # RESET
    # =====================================================

    def reset(self):

        self.data = {

            "bot_status": "STOPPED",

            "symbol": None,

            "positions": [],

            "last_signal": None,

            "profit": 0.0,

            "loss": 0.0,

            "updated": datetime.now()

        }





    # =====================================================
    # SET
    # =====================================================

    def set(
        self,
        key: str,
        value
    ):

        self.data[key] = value

        self.data["updated"] = datetime.now()





    # =====================================================
    # GET
    # =====================================================

    def get(
        self,
        key: str,
        default=None
    ):

        return self.data.get(
            key,
            default
        )





    # =====================================================
    # UPDATE
    # =====================================================

    def update(
        self,
        values: dict
    ):

        self.data.update(
            values
        )

        self.data["updated"] = datetime.now()





    # =====================================================
    # DELETE
    # =====================================================

    def delete(
        self,
        key: str
    ):

        if key in self.data:

            del self.data[key]





    # =====================================================
    # CHECK
    # =====================================================

    def has(
        self,
        key: str
    ) -> bool:

        return key in self.data





    # =====================================================
    # SNAPSHOT
    # =====================================================

    def snapshot(self):

        return deepcopy(
            self.data
        )





# =====================================================
# GLOBAL INSTANCE
# =====================================================

memory = Memory()