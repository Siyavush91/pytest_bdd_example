from pages.BasePO import BasePO
from selenium.webdriver.common.by import By
from . import logger, asserts, constants

class TeamManagementPO(BasePO):
    TEAM_MANAGEMENT_HEADER = (By.XPATH, f"//*[text()='{constants.TEAM_MANAGEMENT_HEADER}']")
    TEAM_MANAGEMENT_DESC = (By.XPATH, f"//*[text()='{constants.TEAM_MANAGEMENT_DESC}']")
    INVITE_EMPLOYEE_EXPAND_BTN = (By.XPATH, f"//*[text()='{constants.INVITE_EMPLOYEE_EXPAND_BTN}']")
    INVITE_EMPLOYEE_COLLAPSE_BTN = (By.XPATH, f"//*[text()='{constants.INVITE_COLLAPSE_BTN}']")
    YOUR_EMLOYEES_TAB = (By.CSS_SELECTOR, "[data-id='team-manage-employees']")
    TEAM_MANAGE_REWARDS_TAB = (By.CSS_SELECTOR, "[data-id='team-manage-rewards']")

    AUTHORIZED_EMLOYEES_TAB = (By.CSS_SELECTOR, "[data-id='team-manage-employees-authorized']")
    PENDING_EMPOYEES_TAB = (By.CSS_SELECTOR, "[data-id='team-manage-employees-pending']")
    BLOCKED_EMPOYEES_TAB = (By.CSS_SELECTOR, "[data-id='team-manage-employees-banned']")
    FIRED_EMPOYEES_TAB = (By.CSS_SELECTOR, "[data-id='team-manage-employees-fired']")
    FIRING_EMPOYEES_TAB = (By.CSS_SELECTOR, "[data-id='team-manage-employees-fire']")

    WALLET_ADDRESS_FIELD = (By.CSS_SELECTOR, "[data-id='permission-request-address-input']")
    WALLET_ADDRESS_LABEL = (By.XPATH, f"//*[text()='{constants.EMPLOYEE_WALLET_ADDRESS_LABEL}']")
    REQUESTED_DOCS_LABEL = (By.XPATH, f"//*[text()='{constants.REQUESTED_DOCS_LABEL}']")
    REQUESTED_DOCS_HEADER = (By.XPATH, f"//*[text()='{constants.REQUESTED_DOCS_HEADER}']")
    AGREE_CHECKBOX = (By.CSS_SELECTOR, "[data-id='permission-request-agree-checkbox']")
    INVITE_BTN = (By.CSS_SELECTOR, "[data-id='permission-request-submit-button']")

    LIST = (By.CLASS_NAME, "employee-list")
    PERMISSION_ADDRESS = (By.CSS_SELECTOR, "div.item__container__info > div")
    PERMISSION_OPEN_BTN = (By.CSS_SELECTOR, "[data-id='team-manage-employee-open']")
    LOADER_UP = (By.CSS_SELECTOR, "div > svg > circle")

    def waiter(self):
        self._wait_elements_displayed([self.TEAM_MANAGEMENT_HEADER, self.YOUR_EMLOYEES_TAB])
        return self

    def verify_connect_partners_page_base(self):
        self._wait_for_element_not_present(self.LOADER_UP)
        self.verify_add_employee_block_collapsed()
        self._wait_elements_displayed([self.YOUR_EMLOYEES_TAB, self.TEAM_MANAGE_REWARDS_TAB, self.LIST])
        self._wait_elements_displayed([self.AUTHORIZED_EMLOYEES_TAB, self.PENDING_EMPOYEES_TAB, self.BLOCKED_EMPOYEES_TAB, self.FIRED_EMPOYEES_TAB, self.FIRING_EMPOYEES_TAB])

        asserts.soft_assert_equal(self._get_element_text(self.YOUR_EMLOYEES_TAB), constants.YOUR_EMLOYEES_TAB)
        asserts.soft_assert_equal(self._get_element_text(self.TEAM_MANAGE_REWARDS_TAB), constants.TEAM_MANAGE_REWARDS_TAB)
        asserts.soft_assert_equal(self._get_element_text(self.AUTHORIZED_EMLOYEES_TAB), constants.AUTHORIZED_EMLOYEES_TAB)
        asserts.soft_assert_equal(self._get_element_text(self.PENDING_EMPOYEES_TAB), constants.PENDING_EMPOYEES_TAB)
        asserts.soft_assert_equal(self._get_element_text(self.BLOCKED_EMPOYEES_TAB), constants.BLOCKED_EMPOYEES_TAB)
        asserts.soft_assert_equal(self._get_element_text(self.FIRED_EMPOYEES_TAB), constants.FIRED_EMPOYEES_TAB)
        asserts.soft_assert_equal(self._get_element_text(self.FIRING_EMPOYEES_TAB), constants.FIRING_EMPOYEES_TAB)
        return self

    def verify_add_employee_block_collapsed(self):
        self._wait_elements_displayed([self.TEAM_MANAGEMENT_HEADER, self.TEAM_MANAGEMENT_DESC, self.INVITE_EMPLOYEE_EXPAND_BTN])
        return self

    def verify_add_employee_block_expanded(self):
        self._wait_elements_displayed([self.TEAM_MANAGEMENT_HEADER, self.TEAM_MANAGEMENT_DESC])
        self._wait_elements_displayed([self.WALLET_ADDRESS_LABEL, self.WALLET_ADDRESS_FIELD, self.REQUESTED_DOCS_LABEL, self.REQUESTED_DOCS_HEADER])
        self._wait_elements_displayed([self.AGREE_CHECKBOX, self.INVITE_BTN, self.INVITE_EMPLOYEE_COLLAPSE_BTN])
        asserts.soft_assert_equal(self._get_placeholder_text(self.WALLET_ADDRESS_FIELD), constants.WALLET_ADDRESS_FIELD_PLACEHOLDER)
        asserts.soft_assert_equal(self._get_element_text(self.AGREE_CHECKBOX), constants.AGREE_CHECKBOX_TEXT)
        asserts.soft_assert_equal(self._get_element_text(self.INVITE_BTN), constants.INVITE_BTN)
        return self

    def wait_active_authorized_employees_tab(self):
        self._wait_element_active(self.AUTHORIZED_EMLOYEES_TAB)
        return self

    def click_add_new_employee(self):
        self._click_element(self.INVITE_EMPLOYEE_EXPAND_BTN)
        return self

    def fill_address(self, address):
        self.driver.find_element(*self.WALLET_ADDRESS_FIELD).send_keys(address)
        return self

    def click_checkbox(self):
        self._click_element(self.AGREE_CHECKBOX)
        return self

    def click_invite_btn(self):
        self._click_element(self.INVITE_BTN)
        return self

    def verify_permission(self, address, status):
        if status == "Data are received":
            locator = (By.XPATH, f"//*[@data-id='{address}']//ancestor::div[@class='item__container']//descendant::div[text()='{constants.DATA_RECEIVED}']")
        elif status == "Invite is sent":
            locator = (By.XPATH, f"//*[@data-id='{address}']//ancestor::div[@class='item__container']//descendant::div[text()='{constants.INVITE_SENT}']")
        elif status == "Access is requested":
            locator = (By.XPATH, f"//*[@data-id='{address}']//ancestor::div[@class='item__container']//descendant::div[text()='{constants.ACCESS_REQUESTED}']")
        else:
            raise('Not supported status')
        self._wait_for_element_present(locator)
        return self

    def verify_permission_grant(self):
        self._wait_for_element_present(self.PERMISSION_OPEN_BTN)
        return self

    def open_permission(self):
        self._click_last_element(self.PERMISSION_OPEN_BTN)
        return self

    def go_to_pending_auth_tab(self):
        self._click_element(self.PENDING_EMPOYEES_TAB)
        return self
