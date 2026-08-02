"""
=========================================================
Gold AI Trading Assistant
Core MetaTrader 5 Engine
=========================================================
"""

from __future__ import annotations

from datetime import datetime

import MetaTrader5 as mt5

from core.logger import Logger

from CONFIG.mt5 import MT5Config



class MT5Engine:


    def __init__(self):

        self.connected = False



    # =====================================================
    # CONNECT
    # =====================================================

    def connect(self):

        try:

            if mt5.initialize():

                self.connected = True

                Logger.info(
                    "MT5 Connected"
                )

                return True



            Logger.error(
                f"MT5 Init Failed: {mt5.last_error()}"
            )

            return False



        except Exception as e:

            Logger.error(
                f"MT5 Error: {e}"
            )

            return False





    # =====================================================
    # DISCONNECT
    # =====================================================

    def disconnect(self):

        mt5.shutdown()

        self.connected = False


        Logger.info(
            "MT5 Disconnected"
        )





    # =====================================================
    # STATUS
    # =====================================================

    def status(self):

        return self.connected





    # =====================================================
    # TERMINAL INFO
    # =====================================================

    def terminal_info(self):

        if not self.connected:

            return None



        info = mt5.terminal_info()


        if info:

            return info._asdict()



        return None





    # =====================================================
    # ACCOUNT INFO
    # =====================================================

    def account_info(self):

        if not self.connected:

            return None



        info = mt5.account_info()


        if info:

            return info._asdict()



        return None





    # =====================================================
    # SYMBOL CHECK
    # =====================================================

    def symbol_check(
        self,
        symbol=None
    ):


        if symbol is None:

            symbol = MT5Config.SYMBOL



        info = mt5.symbol_info(
            symbol
        )


        if info is None:

            return False



        if not info.visible:

            mt5.symbol_select(
                symbol,
                True
            )


        return True





    # =====================================================
    # CURRENT TICK
    # =====================================================

    def get_tick(
        self,
        symbol=None
    ):


        if not self.connected:

            return None



        if symbol is None:

            symbol = MT5Config.SYMBOL



        tick = mt5.symbol_info_tick(
            symbol
        )


        if tick is None:

            return None



        return {


            "symbol": symbol,


            "bid": tick.bid,


            "ask": tick.ask,


            "spread": round(
                tick.ask - tick.bid,
                2
            ),


            "time": datetime.fromtimestamp(
                tick.time
            )

        }





    # =====================================================
    # SPREAD CHECK
    # =====================================================

    def get_spread(
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



        return round(
            tick.ask - tick.bid,
            2
        )





    # =====================================================
    # MARKET READY
    # =====================================================

    def ready(self):


        if not self.connected:

            return False



        return self.symbol_check(
            MT5Config.SYMBOL
        )





# =====================================================
# GLOBAL INSTANCE
# =====================================================

mt5_engine = MT5Engine()