from selenium.webdriver.common.by import By
import time
from . import logger, asserts, constants
from pages.BasePO import BasePO
from modules import header_module

class InviteCompanySetupPO(BasePO):
    COMPANY_SETUP_HEADER = (By.XPATH, f"//*[text()='{constants.COMPANY_SETUP_HEADER}']")
    DESCRIPTION = (By.CLASS_NAME, "company-accept__description")

    STEP_ONE_DESC = (By.XPATH, f"//*[text()='{constants.STEP_ONE_DESC}']")
    SHOW_COMPANY_INFO_TOGGLE = (By.CSS_SELECTOR, "[data-id='company-accept-toggle-button']")
    STEP_TWO_DESC = (By.XPATH, f"//*[text()='{constants.STEP_TWO_DESC}']")
    EXECUTIVE_FLD = (By.CSS_SELECTOR, "[data-id='company-accept-permission-field']")
    STEP_THREE_DESC = (By.XPATH, f"//*[text()='{constants.STEP_THREE_DESC}']")
    SHOW_FOUNDERS_FIELDS_TOGGLE = (By.CSS_SELECTOR, "[data-id='company-accept-toggle-founders-button']")

    INVITE_MEMBERS_BTN = (By.CSS_SELECTOR, "[data-id='company-accept-request-permissions-button']")
    CANCEL_INVITE_BTN = (By.CSS_SELECTOR, "[data-id='company-accept-cancel-permission-button']")

    CANCEL_COMPANY_BTN = (By.CSS_SELECTOR, "button.flat-button.accept-requesting__decline-company")
    FINISH_SETUP_BTN = (By.CSS_SELECTOR, "[data-id='company-accept-accept-company-button']")

    def verify_page(self):
        header_module.verify_header(self)
        self._wait_elements_displayed([self.COMPANY_SETUP_HEADER, self.DESCRIPTION])
        self._wait_elements_displayed([self.STEP_ONE_DESC, self.SHOW_COMPANY_INFO_TOGGLE, self.STEP_TWO_DESC, self.EXECUTIVE_FLD, self.STEP_THREE_DESC, self.SHOW_FOUNDERS_FIELDS_TOGGLE])
        self._wait_elements_displayed([self.INVITE_MEMBERS_BTN, self.CANCEL_COMPANY_BTN])

        asserts.soft_assert_equal(self._get_element_text(self.DESCRIPTION), constants.COMPANY_SETUP_DESCRIPTION)
        asserts.soft_assert_equal(self._get_element_text(self.SHOW_COMPANY_INFO_TOGGLE), constants.SHOW_COMPANY_INFO_TOGGLE)
        asserts.soft_assert_equal(self._get_element_text(self.SHOW_FOUNDERS_FIELDS_TOGGLE), constants.SHOW_FOUNDERS_FIELDS_TOGGLE)
        asserts.soft_assert_equal(self._get_element_text(self.INVITE_MEMBERS_BTN), constants.INVITE_MEMBERS_BTN)
        asserts.soft_assert_equal(self._get_element_text(self.CANCEL_COMPANY_BTN), constants.DECLINE_BTN)
        return self

    def input_executive_address(self, address):
        self.driver.find_element(*self.EXECUTIVE_FLD).clear()
        self.driver.find_element(*self.EXECUTIVE_FLD).send_keys(address)
        return self

    def invite_members(self):
        self._click_element(self.INVITE_MEMBERS_BTN)
        self._wait_for_element_not_present(self.INVITE_MEMBERS_BTN)
        self._wait_for_element_present(self.CANCEL_INVITE_BTN)
        return self

    def verify_invited_members(self):
        self._wait_elements_displayed([self.CANCEL_INVITE_BTN, self.FINISH_SETUP_BTN])
        asserts.assert_equal(self._get_element_text(self.FINISH_SETUP_BTN), constants.FINISH_SETUP)
        return

    def cancel_create_company(self):
        self._click_element(self.CANCEL_COMPANY_BTN)
        return self


    def finish_setup(self):
        self._click_element(self.FINISH_SETUP_BTN)
        return self
