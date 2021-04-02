from .BasePO import BasePO
from selenium.webdriver.common.by import By
from . import logger, asserts, constants

class WelcomePO(BasePO):
    BRAND_LABEL = (By.CLASS_NAME, "auth-container__brand")
    HEADER = (By.XPATH, "//*[text()='Авторизация']")
    DESCRIPTION = (By.CLASS_NAME, "auth-container__block__content")
    BTN_CONT = (By.CSS_SELECTOR, "[data-id='go-to-auth-button']")
    PROGRESS_BAR = (By.CSS_SELECTOR, "div.auth-container__container > div > div > div > svg")

    def waiter(self):
        self._wait_for_element_present(self.BTN_CONT)
        return self
    
    def verify_page(self):
        self._wait_for_elements_present([self.BRAND_LABEL, self.HEADER, self.DESCRIPTION, self.BTN_CONT])
        asserts.soft_assert_equal(self._get_element_text(self.BRAND_LABEL), constants.WELCOME_LABEL)
        asserts.soft_assert_equal(self._get_element_text(self.DESCRIPTION), constants.WELCOME_DESC_AND_BTN)
        return self

    def click_welcome(self):
        self._click_element(self.BTN_CONT)
        return self
    
    def wait_loader_not_displayed(self):
        self._wait_for_element_not_present(self.PROGRESS_BAR)
        return self