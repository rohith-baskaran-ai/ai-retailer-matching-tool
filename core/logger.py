"""
Module:
    Logger

Purpose:
    Centralized logging for the Product Matching Framework.

Responsibilities:
    - Console logging
    - File logging
    - Debug logging
    - Timestamped log files

Author:
    Rohith + ChatGPT

Version:
    1.0
"""

import logging
from datetime import datetime
from pathlib import Path

import config


class Logger:
    """
    Central application logger.

    Features
    --------
    - Console logging
    - File logging
    - Timestamped log files
    - Debug mode support
    """

    def __init__(self):

        # --------------------------------------------------
        # Project Root
        # --------------------------------------------------

        project_root = Path(__file__).resolve().parent.parent

        log_directory = project_root / "logs"

        log_directory.mkdir(exist_ok=True)

        log_file = log_directory / datetime.now().strftime(
            "run_%Y%m%d_%H%M%S.log"
        )

        # --------------------------------------------------
        # Logger
        # --------------------------------------------------

        self.logger = logging.getLogger("ProductMatching")

        level = (
            logging.DEBUG
            if config.DEBUG
            else logging.INFO
        )

        self.logger.setLevel(level)

        # Prevent duplicate logs
        self.logger.propagate = False

        # Prevent duplicate handlers
        if self.logger.handlers:
            return

        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s",
            "%H:%M:%S"
        )

        # --------------------------------------------------
        # File Handler
        # --------------------------------------------------

        file_handler = logging.FileHandler(
            log_file,
            encoding="utf-8"
        )

        file_handler.setFormatter(formatter)

        # --------------------------------------------------
        # Console Handler
        # --------------------------------------------------

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

        self.logger.addHandler(console_handler)

    # ==================================================
    # Logging Methods
    # ==================================================

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)


# ======================================================
# Shared Logger Instance
# ======================================================

logger = Logger()