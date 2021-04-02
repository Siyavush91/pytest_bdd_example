from urllib.parse import urlparse
from .BasePO import BasePO
from selenium.webdriver.common.by import By
from . import logger, asserts, constants

class AdminLoginPO(BasePO):
    BRAND_LABEL = (By.CLASS_NAME, "auth-container__brand")
    HEADER = (By.XPATH, "//*[text()='Авторизация']")
    DESCRIPTION = (By.CLASS_NAME, "auth-container__block__content")
    QR_CODE = (By.CLASS_NAME, "auth__qr")
    YOUR_BIOMETRY = (By.CLASS_NAME, "auth__caption")
    PIN_CODE = (By.CSS_SELECTOR, "[data-id='pin-input']")
    PIN_CODE_PLACEHOLDER = (By.XPATH, "//input[@placeholder='Например, 0000']")
    BTN_AUTH = (By.CSS_SELECTOR, "[data-id='auth-button']")
    PROGRESS_BAR = (By.CSS_SELECTOR, "div.auth-container__container > div > div > div > svg")

    def waiter(self):
        self._wait_for_element_present(self.PIN_CODE)
        return self

    def verify_page(self):
        self._wait_for_elements_present([self.BRAND_LABEL, self.HEADER, self.DESCRIPTION, self.QR_CODE])
        self._wait_for_elements_present([self.YOUR_BIOMETRY, self.PIN_CODE, self.PIN_CODE_PLACEHOLDER, self.BTN_AUTH])
        asserts.soft_assert_equal(self._get_element_text(self.BRAND_LABEL), constants.WELCOME_LABEL)
        asserts.soft_assert_equal(self._get_element_text(self.HEADER), constants.WELCOME_HEADER)
        asserts.soft_assert_equal(self._get_element_text(self.DESCRIPTION), constants.ADMIN_LOGIN_DESC)
        asserts.soft_assert_equal(self._get_element_text(self.YOUR_BIOMETRY), constants.YOUR_BIOMETRY_LABEL)
        asserts.soft_assert_equal(self._get_element_text(self.BTN_AUTH), constants.ADMIN_LOGIN_BTN)
        return self

    def input_pin(self, pin):
        self.driver.find_element(*self.PIN_CODE).send_keys(pin)
        return self


    def login(self):
        self.click_element_by_mouse(self.BTN_AUTH)
        return self


    def login_button_tappable(self):
        self._is_element_enabled(*self.BTN_AUTH)
        return self

    def wait_loader_not_displayed(self):
        self._wait_for_element_not_present(self.PROGRESS_BAR)
        return self
