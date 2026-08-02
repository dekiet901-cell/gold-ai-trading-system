"""
=========================================================
Gold AI Trading Assistant
Core Realtime Engine
=========================================================
"""

from __future__ import annotations

import time
import threading

from typing import Callable, List



class RealtimeEngine:


    def __init__(self):

        self.running = False

        self.callbacks: List[Callable] = []

        self.thread = None



    # =====================================================
    # REGISTER CALLBACK
    # =====================================================

    def register(
        self,
        callback: Callable
    ):

        if callback not in self.callbacks:

            self.callbacks.append(
                callback
            )



    # =====================================================
    # REMOVE CALLBACK
    # =====================================================

    def unregister(
        self,
        callback: Callable
    ):

        if callback in self.callbacks:

            self.callbacks.remove(
                callback
            )



    # =====================================================
    # PROCESS LOOP
    # =====================================================

    def loop(self):

        while self.running:


            for callback in self.callbacks:

                try:

                    callback()


                except Exception as e:

                    print(
                        f"Realtime Error: {e}"
                    )


            time.sleep(0.1)



    # =====================================================
    # START
    # =====================================================

    def start(self):

        if self.running:

            return False


        self.running = True


        self.thread = threading.Thread(

            target=self.loop,

            daemon=True

        )


        self.thread.start()


        return True



    # =====================================================
    # STOP
    # =====================================================

    def stop(self):

        self.running = False


        if self.thread:

            self.thread.join(
                timeout=2
            )


        self.thread = None



    # =====================================================
    # STATUS
    # =====================================================

    def status(self):

        return self.running





# =====================================================
# GLOBAL INSTANCE
# =====================================================

realtime = RealtimeEngine()