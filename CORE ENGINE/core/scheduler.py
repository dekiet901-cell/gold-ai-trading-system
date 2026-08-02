"""
=========================================================
Gold AI Trading Assistant
Core Scheduler Engine
=========================================================
"""

from __future__ import annotations

import time
import threading

from typing import Callable, List





class Scheduler:

    """
    Central Task Scheduler
    """



    def __init__(self):

        self.tasks: List[dict] = []

        self.running = False

        self.thread = None





    # =====================================================
    # ADD TASK
    # =====================================================

    def add_task(
        self,
        name: str,
        function: Callable,
        interval: float
    ):


        for task in self.tasks:

            if task["name"] == name:

                return False



        self.tasks.append(

            {
                "name": name,
                "function": function,
                "interval": interval,
                "last_run": 0
            }

        )


        return True





    # =====================================================
    # REMOVE TASK
    # =====================================================

    def remove_task(
        self,
        name: str
    ):


        self.tasks = [

            task

            for task in self.tasks

            if task["name"] != name

        ]





    # =====================================================
    # RUN LOOP
    # =====================================================

    def run_loop(self):


        while self.running:


            current_time = time.time()



            for task in self.tasks:


                if (

                    current_time
                    -
                    task["last_run"]

                    >=

                    task["interval"]

                ):


                    try:

                        task["function"]()


                    except Exception as e:

                        print(
                            f"Scheduler Error [{task['name']}]: {e}"
                        )



                    task["last_run"] = current_time



            time.sleep(0.1)





    # =====================================================
    # START
    # =====================================================

    def start(self):


        if self.running:

            return False



        self.running = True



        self.thread = threading.Thread(

            target=self.run_loop,

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
    # COUNT TASK
    # =====================================================

    def count(self):

        return len(
            self.tasks
        )





# =====================================================
# GLOBAL INSTANCE
# =====================================================

scheduler = Scheduler()