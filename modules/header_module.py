from selenium.webdriver.common.by import By
from pages.BasePO import BasePO
from . import logger, asserts, constants
import re


LOGO = (By.CSS_SELECTOR, "svg")
WALLET_WIDGET_TITLE = (By.XPATH, "//span['Временный кошелек'][1]")
WALLET_WIDGET_BALANCE = (By.XPATH, "//span['Временный кошелек'][2]")
LANG_SWITCHER = (By.CSS_SELECTOR, "div.header__Buttons-w5hoxq-1.bzNIzE > button:nth-child(1)")
LOGOUT_BTN = (By.CSS_SELECTOR, "[data-id='user-menu-logout-button']")

def verify_header(self):
    self._wait_for_elements_present([WALLET_WIDGET_TITLE, WALLET_WIDGET_BALANCE, LANG_SWITCHER])
    asserts.soft_assert_equal(self._get_element_text(WALLET_WIDGET_TITLE), constants.WALLET_WIDGET_TITLE)
    asserts.assert_is_not_none(re.match(r'^.+ETH$', self._get_element_text(WALLET_WIDGET_BALANCE)))
