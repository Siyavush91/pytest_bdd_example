from selenium.webdriver.common.by import By
from . import logger, asserts, constants
from modules import header_module, side_menu_module
from pages.BasePO import BasePO


class AdminMainPagePO(BasePO):
    TEAM_CONTAINER = (By.CLASS_NAME, "team")
    ADD_MEMBER_HEADER = (By.XPATH, f"//*[text()='{constants.ADD_MEMBER_HEADER}']")
    ADD_MEMBER_DESC = (By.XPATH, f"//*[text()='{constants.ADD_MEMBER_DESC}']")
    ADD_MEMBER_BTN = (By.XPATH, f"//*[text()='{constants.ADD_MEMBER_BTN}']")

    TEAM_EMPLOYEES_TAB = (By.CSS_SELECTOR, "[data-id='team-manage-employees']")
    TEAM_REWARDS_TAB = (By.CSS_SELECTOR, "[data-id='team-manage-rewards']")

    AUTH_EMPLOYEES_TAB = (By.CSS_SELECTOR, "[data-id='team-manage-employees-authorized']")
    PENDING_EMPLOYEES_TAB = (By.CSS_SELECTOR, "[data-id='team-manage-employees-pending']")
    BANNED_EMPLOYEES_TAB = (By.CSS_SELECTOR, "[data-id='team-manage-employees-banned']")
    FIRED_EMPLOYEES_TAB = (By.CSS_SELECTOR, "[data-id='team-manage-employees-fired']")
    RESIGNING_EMPLOYEES_TAB = (By.CSS_SELECTOR, "[data-id='team-manage-employees-fire']")

    EMPLOYEE_LIST = (By.CLASS_NAME, "employee-list")
    EMPLOYEE_LIST_EMPTY = (By.CLASS_NAME, "employee-list__empty")

    def waiter(self):
        self._wait_for_elements_present([self.ADD_MEMBER_BTN, self.EMPLOYEE_LIST])
        return self

    def verify_admin_page(self):
        side_menu_module.verify_admin_side_menu(self)
        header_module.verify_header(self)
        self._wait_for_elements_present([self.TEAM_CONTAINER, self.ADD_MEMBER_HEADER, self.ADD_MEMBER_DESC, self.ADD_MEMBER_BTN])
        self._wait_for_elements_present([self.TEAM_EMPLOYEES_TAB, self.TEAM_REWARDS_TAB])
        self._wait_for_elements_present([self.AUTH_EMPLOYEES_TAB, self.PENDING_EMPLOYEES_TAB, self.BANNED_EMPLOYEES_TAB, self.FIRED_EMPLOYEES_TAB, self.RESIGNING_EMPLOYEES_TAB, self.EMPLOYEE_LIST])
        asserts.soft_assert_equal(self._get_element_text(self.ADD_MEMBER_HEADER), constants.ADD_MEMBER_HEADER)
        asserts.soft_assert_equal(self._get_element_text(self.ADD_MEMBER_DESC), constants.ADD_MEMBER_DESC)
        asserts.soft_assert_equal(self._get_element_text(self.ADD_MEMBER_BTN), constants.ADD_MEMBER_BTN)

        asserts.soft_assert_equal(self._get_element_text(self.TEAM_EMPLOYEES_TAB), constants.TEAM_EMPLOYEES_TAB)
        asserts.soft_assert_equal(self._get_element_text(self.TEAM_REWARDS_TAB), constants.TEAM_REWARDS_TAB)

        asserts.soft_assert_equal(self._get_element_text(self.AUTH_EMPLOYEES_TAB), constants.AUTH_EMPLOYEES_TAB)
        asserts.soft_assert_equal(self._get_element_text(self.PENDING_EMPLOYEES_TAB), constants.PENDING_EMPLOYEES_TAB)
        asserts.soft_assert_equal(self._get_element_text(self.BANNED_EMPLOYEES_TAB), constants.BANNED_EMPLOYEES_TAB)
        asserts.soft_assert_equal(self._get_element_text(self.FIRED_EMPLOYEES_TAB), constants.FIRED_EMPLOYEES_TAB)
        asserts.soft_assert_equal(self._get_element_text(self.RESIGNING_EMPLOYEES_TAB), constants.RESIGNING_EMPLOYEES_TAB)
        return self

    def verify_empty_employee_list(self):
        self._wait_for_elements_present([self.EMPLOYEE_LIST_EMPTY])
        asserts.soft_assert_equal(self._get_element_text(self.EMPLOYEE_LIST_EMPTY), constants.EMPLOYEE_LIST_EMPTY)
        return self
