"""
Module:
    Browser

Purpose:
    Central browser interface for the Product Matching Framework.

Responsibilities:
    - Own WebDriver
    - Own Finder
    - Navigation
    - Page access
    - Element access
    - Tab management
    - Graceful shutdown

Author:
    Rohith + ChatGPT

Version:
    1.0
"""

import time

import config
from core.driver import create_driver
from core.finder import Finder
from core.logger import logger


class Browser:

    def __init__(self):

        self._driver = None

        self._finder = None

        self._tabs = {}

    # ==================================================
    # Lifecycle
    # ==================================================

    def start(self):

        logger.info("[Browser] Starting Browser")

        self._driver = create_driver()

        self._finder = Finder(self._driver)

    def quit(self):

        logger.info("[Browser] Closing Browser")

        if self._driver is None:
            return

        try:

            self._driver.quit()

        except Exception:

            logger.warning("[Browser] Browser already closed")

    # ==================================================
    # Navigation
    # ==================================================

    def open(self, url):

        logger.info(f"[Browser] Opening: {url}")

        self._driver.get(url)

        time.sleep(config.PAGE_STABILIZE_TIME)

    def back(self):

        self._driver.back()

    def refresh(self):

        self._driver.refresh()

    # ==================================================
    # Page Information
    # ==================================================

    def url(self):

        return self._driver.current_url

    def title(self):

        return self._driver.title

    def html(self):

        return self._driver.page_source

    # ==================================================
    # Finder Delegation
    # ==================================================

    def find(self, selector, **kwargs):

        return self._finder.element(selector, **kwargs)

    def find_all(self, selector, **kwargs):

        return self._finder.elements(selector, **kwargs)

    def text(self, selector, **kwargs):

        return self._finder.text(selector, **kwargs)

    def attribute(self, selector, attribute, **kwargs):

        return self._finder.attribute(
            selector,
            attribute,
            **kwargs
        )

    def exists(self, selector, **kwargs):

        return self._finder.exists(selector, **kwargs)

    def click(self, selector, **kwargs):

        self._finder.click(selector, **kwargs)

    # ==================================================
    # Tabs
    # ==================================================

    def new_tab(self):

        self._driver.switch_to.new_window("tab")

    def save_tab(self, name):

        self._tabs[name] = self._driver.current_window_handle

    def switch_tab(self, name):

        self._driver.switch_to.window(
            self._tabs[name]
        )

    def close_current_tab(self):

        self._driver.close()