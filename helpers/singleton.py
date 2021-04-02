"""Singleton for driver"""

import logging
from selenium.webdriver import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# pylint: disable=too-few-public-methods
class Wrapper(type):
    """Wrapper for driver"""
    instance = None
    connection = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Wrapper, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def webdriver_rem(self):
        """Init driver"""
        self.connection = webdriver.Chrome(ChromeDriverManager().install())
        return self.connection
