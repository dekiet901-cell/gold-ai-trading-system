"""
=========================================================
Gold AI Trading Assistant
Core Event Engine
=========================================================
"""

from __future__ import annotations

from typing import Callable, Dict, List



class EventBus:
    """
    Central Event Manager

    MT5 -> Data -> Strategy -> Execution
    """



    def __init__(self):

        self.events: Dict[str, List[Callable]] = {}



    # =====================================================
    # REGISTER EVENT
    # =====================================================

    def subscribe(
        self,
        event_name: str,
        callback: Callable
    ):

        if event_name not in self.events:

            self.events[event_name] = []


        if callback not in self.events[event_name]:

            self.events[event_name].append(callback)



    # =====================================================
    # REMOVE EVENT
    # =====================================================

    def unsubscribe(
        self,
        event_name: str,
        callback: Callable
    ):

        if event_name in self.events:

            if callback in self.events[event_name]:

                self.events[event_name].remove(callback)



    # =====================================================
    # EMIT EVENT
    # =====================================================

    def emit(
        self,
        event_name: str,
        *args,
        **kwargs
    ):

        if event_name not in self.events:

            return


        for callback in self.events[event_name]:

            try:

                callback(
                    *args,
                    **kwargs
                )


            except Exception as e:

                print(
                    f"EVENT ERROR [{event_name}]: {e}"
                )



    # =====================================================
    # CHECK EVENT
    # =====================================================

    def has(
        self,
        event_name: str
    ) -> bool:

        return event_name in self.events



    # =====================================================
    # COUNT CALLBACK
    # =====================================================

    def count(
        self,
        event_name: str
    ) -> int:

        if event_name not in self.events:

            return 0


        return len(
            self.events[event_name]
        )



    # =====================================================
    # CLEAR
    # =====================================================

    def clear(self):

        self.events.clear()



# =====================================================
# GLOBAL INSTANCE
# =====================================================

event_bus = EventBus()