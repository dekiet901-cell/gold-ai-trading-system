"""
=========================================================
Gold AI Trading Assistant
Core Market State Engine
=========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from CONFIG.mt5 import MT5Config



# =====================================================
# MARKET SNAPSHOT
# =====================================================

@dataclass
class MarketSnapshot:

    symbol: str

    bid: float = 0.0

    ask: float = 0.0

    spread: float = 0.0

    last_update: datetime | None = None

    is_open: bool = False

    volatility: float = 0.0





# =====================================================
# MARKET ENGINE
# =====================================================

class MarketEngine:


    def __init__(self):

        self.snapshot = MarketSnapshot(
            symbol=MT5Config.SYMBOL
        )



    # =================================================
    # UPDATE MARKET
    # =================================================

    def update(
        self,
        bid: float,
        ask: float,
        volatility: float = 0.0
    ):

        self.snapshot.bid = bid

        self.snapshot.ask = ask

        self.snapshot.spread = round(
            ask - bid,
            5
        )

        self.snapshot.volatility = volatility

        self.snapshot.last_update = datetime.now()

        self.snapshot.is_open = True



    # =================================================
    # UPDATE FROM TICK
    # =================================================

    def update_tick(
        self,
        tick
    ):

        if tick is None:

            return False


        # Tick object từ data.py

        self.update(

            bid=float(tick.bid),

            ask=float(tick.ask)

        )


        return True



    # =================================================
    # PRICE
    # =================================================

    def price(self):

        return {

            "symbol": self.snapshot.symbol,

            "bid": self.snapshot.bid,

            "ask": self.snapshot.ask,

            "spread": self.snapshot.spread

        }



    # =================================================
    # STATUS
    # =================================================

    def status(self):

        return self.snapshot



    # =================================================
    # MARKET OPEN
    # =================================================

    def is_open(self):

        return self.snapshot.is_open



    # =================================================
    # CLOSE MARKET
    # =================================================

    def close(self):

        self.snapshot.is_open = False





# =====================================================
# GLOBAL INSTANCE
# =====================================================

market = MarketEngine()