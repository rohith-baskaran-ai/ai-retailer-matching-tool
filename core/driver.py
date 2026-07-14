"""
Module:
    Driver

Purpose:
    Create and configure the Chrome WebDriver.

Responsibilities:
    - Configure Chrome
    - Create WebDriver
    - Return WebDriver

Author:
    Rohith + ChatGPT

Version:
    1.0
"""

import undetected_chromedriver as uc

import config
from core.logger import logger


def create_driver():
    """
    Create and configure a Chrome WebDriver.
    """

    logger.info("[Driver] Starting Chrome")

    options = uc.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    options.page_load_strategy = "eager"

    if config.HEADLESS:
        options.add_argument("--headless=new")

    try:

        driver = uc.Chrome(
            options=options,
            version_main=config.CHROME_VERSION
        )

        driver.set_page_load_timeout(
            config.PAGE_LOAD_TIMEOUT
        )

        logger.info("[Driver] Chrome Started")

        return driver

    except Exception as error:

        logger.error(
            f"[Driver] Failed to start Chrome: {error}"
        )

        raise