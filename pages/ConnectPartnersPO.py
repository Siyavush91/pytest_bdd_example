from selenium.webdriver.common.by import By
from . import logger, asserts, constants
from pages.BasePO import BasePO
from modules import header_module, side_menu_module
import time


class ConnectPartnersPO(BasePO):
    PERMISSION_ADDRESS = (By.CSS_SELECTOR, "[data-id='partners-list-item-executive']")#need rebese on id by address
    PERMISSION_OPEN_BTN = (By.CSS_SELECTOR, "[data-id='partners-info-register-link-button']")

    LOADER_UP = (By.CSS_SELECTOR, "div > svg > circle")
    INVITE_HEADER = (By.XPATH, f"//*[text()='{constants.INVITE_HEADER}']")
    INVITE_DESC = (By.XPATH, f"//*[text()='{constants.INVITE_DESC}']")
    INVITE_ABOUT = (By.XPATH, f"//*[text()='{constants.INVITE_ABOUT}']")
    INVITE_EXPAND_BTN = (By.XPATH, f"//*[text()='{constants.INVITE_EXPAND_BTN}']")
    YOUR_PARTNERS_TAB = (By.CSS_SELECTOR, "[data-id='partners-info-invited-tab']")
    REQUESTED_PARTNERS_TAB = (By.CSS_SELECTOR, "[data-id='partners-info-requested-tab']")
    LIST = (By.CSS_SELECTOR, "[data-id='partners-list']")

    WALLET_ADDRESS_LABEL = (By.XPATH, f"//*[text()='{constants.WALLET_ADDRESS_LABEL}']")
    WALLET_ADDRESS_FIELD = (By.CSS_SELECTOR, "[data-id='permission-request-address-input']")
    REQUESTED_DOCS_LABEL = (By.XPATH, f"//*[text()='{constants.REQUESTED_DOCS_LABEL}']")
    REQUESTED_DOCS_HEADER = (By.XPATH, f"//*[text()='{constants.REQUESTED_DOCS_HEADER}']")
    COMPANY_NAME_LABEL = (By.XPATH, f"//*[text()='{constants.COMPANY_NAME_LABEL}']")
    COMPANY_NAME_FIELD = (By.CSS_SELECTOR, "[data-id='partners-invite-company-input']")
    AGREE_CHECKBOX = (By.CSS_SELECTOR, "[data-id='permission-request-agree-checkbox']")
    INVITE_BTN = (By.CSS_SELECTOR, "[data-id='permission-request-submit-button']")
    INVITE_COLLAPSE_BTN = (By.XPATH, f"//*[text()='{constants.INVITE_COLLAPSE_BTN}']")

    PARTNER_LIST_COMPANY_NAME = (By.CSS_SELECTOR, "[data-id='partners-list-item-company-name']")
    PARTNER_LIST_DATE = (By.CLASS_NAME, "left-side__date")
    PARTNER_LIST_TITLE = (By.CLASS_NAME, "left-side__name-title")
    PARTNER_LIST_ADDRESS = (By.CLASS_NAME, "left-side__name")
    PARTNER_LIST_STATUS = (By.CLASS_NAME, "partners-list-item-container__right-content")

    def waiter(self):
        self._wait_elements_displayed([self.INVITE_HEADER, self.YOUR_PARTNERS_TAB])
        return self

    def verify_connect_partners_page_base(self):
        self._wait_for_element_not_present(self.LOADER_UP)
        self.verify_add_partner_block_collapsed()
        self._wait_elements_displayed([self.YOUR_PARTNERS_TAB, self.REQUESTED_PARTNERS_TAB, self.LIST])
        return self

    def verify_add_partner_block_collapsed(self):
        self._wait_elements_displayed([self.INVITE_HEADER, self.INVITE_DESC, self.INVITE_ABOUT, self.INVITE_EXPAND_BTN])
        return self

    def verify_add_partner_block_expanded(self):
        self._wait_elements_displayed([self.INVITE_HEADER, self.INVITE_DESC, self.INVITE_ABOUT])
        self._wait_elements_displayed([self.WALLET_ADDRESS_LABEL, self.WALLET_ADDRESS_FIELD, self.REQUESTED_DOCS_LABEL, self.REQUESTED_DOCS_HEADER])
        self._wait_elements_displayed([self.COMPANY_NAME_LABEL, self.COMPANY_NAME_FIELD, self.AGREE_CHECKBOX, self.INVITE_BTN, self.INVITE_COLLAPSE_BTN])
        asserts.soft_assert_equal(self._get_placeholder_text(self.WALLET_ADDRESS_FIELD), constants.WALLET_ADDRESS_FIELD_PLACEHOLDER)
        asserts.soft_assert_equal(self._get_placeholder_text(self.COMPANY_NAME_FIELD), constants.COMPANY_NAME_FIELD_PLACEHOLDER)
        asserts.soft_assert_equal(self._get_element_text(self.AGREE_CHECKBOX), constants.AGREE_CHECKBOX_TEXT)
        asserts.soft_assert_equal(self._get_element_text(self.INVITE_BTN), constants.INVITE_BTN)
        return self

    def check_permisson_dissapeared(self, expected_company_address):
        PERMISSION = self.driver.find_elements(*self.PARTNER_LIST_ADDRESS)
        asserts.assert_not_equal((PERMISSION[-1]).text, expected_company_address)
        return self

    def fill_address(self, address):
        self.driver.find_element(*self.WALLET_ADDRESS_FIELD).send_keys(address)
        return self

    def fill_company_name(self, company_name):
        self.driver.find_element(*self.COMPANY_NAME_FIELD).send_keys(company_name)
        return self

    def click_checkbox(self):
        self._click_element(self.AGREE_CHECKBOX)
        return self

    def click_add_new_partner(self):
        self._click_element(self.INVITE_EXPAND_BTN)
        return self

    def click_invite_btn(self):
        self._click_element(self.INVITE_BTN)
        return self

    def verify_invited_company(self, expected_company_name, expected_company_address, expected_status):
        self._wait_elements_displayed([self.YOUR_PARTNERS_TAB, self.REQUESTED_PARTNERS_TAB, self.LIST])
        self._wait_elements_displayed([self.PARTNER_LIST_COMPANY_NAME, self.PARTNER_LIST_TITLE, self.PARTNER_LIST_ADDRESS, self.PARTNER_LIST_STATUS])
        self._wait_element_active(self.REQUESTED_PARTNERS_TAB)

        last_company_name_from_list = self.driver.find_elements(*self.PARTNER_LIST_COMPANY_NAME)
        last_status_from_list = self.driver.find_elements(*self.PARTNER_LIST_STATUS)
        invited_address_from_list = (By.CSS_SELECTOR, f"[data-id='{expected_company_address}']")
        self._wait_element_displayed(invited_address_from_list)
        asserts.assert_equal((last_company_name_from_list[-1]).text, expected_company_name)
        asserts.assert_equal((last_status_from_list[-1]).text, expected_status)
        return self

    def open_permission(self):
        self._click_last_element(self.PERMISSION_OPEN_BTN)
        return self
