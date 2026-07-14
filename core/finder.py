"""
Module:
    Finder

Purpose:
    Provide a thin wrapper around Selenium element operations.

Responsibilities:
    - Locate elements
    - Wait for elements
    - Read text
    - Read attributes
    - Click elements
    - Check existence

Author:
    Rohith + ChatGPT

Version:
    1.0
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config


class Finder:

    def __init__(self, driver):

        self._driver = driver

    def element(
        self,
        selector,
        by=By.CSS_SELECTOR,
        timeout=config.ELEMENT_TIMEOUT
    ):

        return WebDriverWait(
            self._driver,
            timeout
        ).until(
            EC.presence_of_element_located(
                (by, selector)
            )
        )

    def elements(
        self,
        selector,
        by=By.CSS_SELECTOR,
        timeout=config.ELEMENT_TIMEOUT
    ):

        WebDriverWait(
            self._driver,
            timeout
        ).until(
            EC.presence_of_element_located(
                (by, selector)
            )
        )

        return self._driver.find_elements(
            by,
            selector
        )

    def text(
        self,
        selector,
        by=By.CSS_SELECTOR,
        timeout=config.ELEMENT_TIMEOUT
    ):

        try:

            return self.element(
                selector,
                by,
                timeout
            ).text.strip()

        except Exception:

            return ""

    def attribute(
        self,
        selector,
        attribute,
        by=By.CSS_SELECTOR,
        timeout=config.ELEMENT_TIMEOUT
    ):

        try:

            return self.element(
                selector,
                by,
                timeout
            ).get_attribute(attribute)

        except Exception:

            return ""

    def exists(
        self,
        selector,
        by=By.CSS_SELECTOR
    ):

        try:

            self._driver.find_element(
                by,
                selector
            )

            return True

        except Exception:

            return False

    def click(
        self,
        selector,
        by=By.CSS_SELECTOR,
        timeout=config.ELEMENT_TIMEOUT
    ):

        self.element(
            selector,
            by,
            timeout
        ).click()

    def html(self):

        return self._driver.page_source