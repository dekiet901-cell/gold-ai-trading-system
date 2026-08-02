"""
=========================================================
Gold AI Trading Assistant
Core Market Data Engine
=========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

import MetaTrader5 as mt5

from CONFIG.mt5 import MT5Config



# =====================================================
# CANDLE DATA
# =====================================================

@dataclass
class Candle:

    time: datetime

    open: float

    high: float

    low: float

    close: float

    volume: float = 0





# =====================================================
# TICK DATA
# =====================================================

@dataclass
class Tick:

    time: datetime

    bid: float

    ask: float





# =====================================================
# DATA ENGINE
# =====================================================

class DataEngine:


    def __init__(self):

        self.candles: List[Candle] = []

        self.ticks: List[Tick] = []

        self.max_history = MT5Config.HISTORY_BARS





    # =================================================
    # ADD CANDLE
    # =================================================

    def add_candle(
        self,
        candle: Candle
    ):

        self.candles.append(
            candle
        )


        if len(self.candles) > self.max_history:

            self.candles.pop(0)





    # =================================================
    # ADD TICK
    # =================================================

    def add_tick(
        self,
        tick: Tick
    ):

        self.ticks.append(
            tick
        )


        if len(self.ticks) > 1000:

            self.ticks.pop(0)





    # =================================================
    # GET MT5 TICK
    # =================================================

    def fetch_tick(
        self,
        symbol=None
    ):


        if symbol is None:

            symbol = MT5Config.SYMBOL



        tick = mt5.symbol_info_tick(
            symbol
        )


        if tick is None:

            return None



        data = Tick(

            time=datetime.fromtimestamp(
                tick.time
            ),

            bid=tick.bid,

            ask=tick.ask

        )


        self.add_tick(
            data
        )


        return data





    # =================================================
    # GET MT5 CANDLES
    # =================================================

    def fetch_candles(
        self,
        timeframe=mt5.TIMEFRAME_M1,
        count=None,
        symbol=None
    ):


        if symbol is None:

            symbol = MT5Config.SYMBOL



        if count is None:

            count = MT5Config.HISTORY_BARS



        rates = mt5.copy_rates_from_pos(

            symbol,

            timeframe,

            0,

            count

        )


        if rates is None:

            return []



        result = []



        for row in rates:


            candle = Candle(

                time=datetime.fromtimestamp(
                    row["time"]
                ),

                open=float(row["open"]),

                high=float(row["high"]),

                low=float(row["low"]),

                close=float(row["close"]),

                volume=float(row["tick_volume"])

            )


            result.append(
                candle
            )



        self.candles = result[-self.max_history:]



        return self.candles





    # =================================================
    # LAST CANDLE
    # =================================================

    def latest_candle(
        self
    ) -> Optional[Candle]:


        if not self.candles:

            return None



        return self.candles[-1]





    # =================================================
    # CLEAR DATA
    # =================================================

    def clear(self):

        self.candles.clear()

        self.ticks.clear()





    # =================================================
    # COUNT
    # =================================================

    def candle_count(self):

        return len(
            self.candles
        )





# =====================================================
# GLOBAL INSTANCE
# =====================================================

data_engine = DataEngine()