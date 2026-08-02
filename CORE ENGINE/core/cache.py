"""
=========================================================
Gold AI Trading Assistant
Core Cache Engine
=========================================================
"""

from __future__ import annotations

from datetime import datetime





class Cache:


    def __init__(self):

        self.storage = {}





    # =====================================================
    # SET DATA
    # =====================================================

    def set(
        self,
        key: str,
        value,
        expire: int | None = None
    ):

        self.storage[key] = {

            "value": value,

            "time": datetime.now(),

            "expire": expire

        }





    # =====================================================
    # GET DATA
    # =====================================================

    def get(
        self,
        key: str,
        default=None
    ):


        if key not in self.storage:

            return default



        item = self.storage[key]



        expire = item["expire"]



        if expire is not None:


            elapsed = (

                datetime.now()

                -

                item["time"]

            ).total_seconds()



            if elapsed >= expire:

                self.delete(key)

                return default





        return item["value"]





    # =====================================================
    # CHECK KEY
    # =====================================================

    def has(
        self,
        key: str
    ) -> bool:

        return key in self.storage





    # =====================================================
    # DELETE
    # =====================================================

    def delete(
        self,
        key: str
    ):


        if key in self.storage:

            del self.storage[key]





    # =====================================================
    # CLEAR
    # =====================================================

    def clear(self):

        self.storage.clear()





    # =====================================================
    # SIZE
    # =====================================================

    def size(self):

        return len(
            self.storage
        )





# =====================================================
# GLOBAL INSTANCE
# =====================================================

cache = Cache()