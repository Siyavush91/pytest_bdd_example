from selenium.webdriver.common.by import By

from . import logger, asserts, constants
from pages.BasePO import BasePO
from modules import header_module

class InvitePolicyPO(BasePO):
    POLICY_HEADER = (By.XPATH, f"//*[text()='{constants.POLICY_HEADER}']")
    POLICY_CONTAINER = (By.CLASS_NAME, "policy")
    CHECKBOX = (By.CSS_SELECTOR, "[data-id='invite-policy-accept-agree-checkbox']")
    CHECKBOX_TEXT = (By.XPATH, f"//*[text()='{constants.CHECKBOX_TEXT}']")
    NEXT_BTN = (By.CSS_SELECTOR, "[data-id='invite-policy-accept-accept-button']")

    def verify_page(self):
        header_module.verify_header(self)
        self._wait_elements_displayed([self.POLICY_HEADER, self.POLICY_CONTAINER, self.NEXT_BTN, self.CHECKBOX, self.CHECKBOX_TEXT])
        asserts.soft_assert_equal(self._get_element_text(self.NEXT_BTN), constants.INVITE_POLICY_NEXT_BTN)
        return self

    def click_agree_checkbox(self):
        self._click_element(self.CHECKBOX)
        return self

    def click_next_btn(self):
        self._click_element(self.NEXT_BTN)
        return self


