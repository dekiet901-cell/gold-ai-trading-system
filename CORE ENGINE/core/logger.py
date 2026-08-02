"""
=========================================================
Gold AI Trading Assistant
Core Logger Engine
=========================================================
"""

from __future__ import annotations

import logging
from pathlib import Path

from CONFIG.system import SystemConfig


class Logger:
    """
    Central Logger
    """

    _initialized: bool = False

    @classmethod
    def initialize(cls) -> None:
        """
        Initialize logging system.
        """

        if cls._initialized:
            return

        # Create log directory
        SystemConfig.LOGS_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        # Configure logger
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[
                logging.FileHandler(
                    SystemConfig.BOT_LOG,
                    encoding="utf-8",
                ),
                logging.StreamHandler(),
            ],
        )

        cls._initialized = True

        logging.info("Logger initialized.")

    @staticmethod
    def info(message: str) -> None:
        logging.info(message)

    @staticmethod
    def warning(message: str) -> None:
        logging.warning(message)

    @staticmethod
    def error(message: str) -> None:
        logging.error(message)

    @staticmethod
    def debug(message: str) -> None:
        logging.debug(message)

    @staticmethod
    def critical(message: str) -> None:
        logging.critical(message)

    @staticmethod
    def exception(message: str) -> None:
        logging.exception(message)