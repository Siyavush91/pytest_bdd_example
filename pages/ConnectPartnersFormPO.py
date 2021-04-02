from selenium.webdriver.common.by import By

from . import logger, asserts, constants
from pages.BasePO import BasePO

class ConnectPartnersFormPO(BasePO):
    PARTNERS_FORM_HEADER = (By.XPATH, f"//*[text()='{constants.PARTNERS_FORM_HEADER}']")
    COMPANY_NAME_TITLE = (By.XPATH, f"//*[text()='{constants.COMPANY_NAME_TITLE}']")
    FOUNDER_INFO_HEADER = (By.CLASS_NAME, "company-votings-item-sublist__title")
    ACCEPT_BTN = (By.CSS_SELECTOR, "[data-id='partners-register-confirm-button']")
    DECLINE_BTN = (By.CSS_SELECTOR, "[data-id='partners-register-decline-button']")

    def waiter(self):
        self._wait_for_element_present(self.PARTNERS_FORM_HEADER)
        return self

    def verify_form(self, company_name):
        self._wait_for_elements_present([self.PARTNERS_FORM_HEADER, self.COMPANY_NAME_TITLE, self.FOUNDER_INFO_HEADER, self.ACCEPT_BTN, self.DECLINE_BTN])
        asserts.soft_assert_equal(self._get_element_text(self.FOUNDER_INFO_HEADER), constants.FOUNDER_INFO_HEADER)
        asserts.soft_assert_equal(self._get_element_text(self.ACCEPT_BTN), constants.ACCEPT_BTN)
        asserts.soft_assert_equal(self._get_element_text(self.DECLINE_BTN), constants.DECLINE_BTN)
        return

    def click_accept_btn(self):
        self._click_element(self.ACCEPT_BTN)
        return self

    def click_decline_btn(self):
        self._click_element(self.DECLINE_BTN)
        return self
