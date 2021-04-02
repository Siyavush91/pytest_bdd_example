from pages.BasePO import BasePO
from selenium.webdriver.common.by import By
from . import logger, asserts, constants


class TeamManagementFormPO(BasePO):
    TEAM_MANAGEMENT_FORM_HEADER = (By.XPATH, f"//*[text()='{constants.TEAM_MANAGEMENT_FORM_HEADER}']")
    DOCUMENT_FORM_HEADER = (By.XPATH, f"//*[text()='{constants.DOCUMENT_FORM_HEADER}']")
    DOCUMENT_FORM = (By.CSS_SELECTOR, "[data-id='document-info-root']")
    ACTIVITY_MANAGEMENT_HEADER = (By.XPATH, f"//*[text()='{constants.ACTIVITY_MANAGEMENT_HEADER}']")
    DECLINE_BTN = (By.CSS_SELECTOR, "[data-id='team-manage-employee-decline']") 
    ACTIVITY_MANAGEMENT_FOOTER = (By.XPATH, f"//*[text()='{constants.ACTIVITY_MANAGEMENT_FOOTER}']")
    ROLE_MANAGEMENT_HEADER = (By.XPATH, f"//*[text()='{constants.ROLE_MANAGEMENT_HEADER}']")
    INVITE_MANAGER_BTN = (By.CSS_SELECTOR, "[data-id='team-manage-invite-to-manager']")
    INVITE_EMPLOYEE_BTN = (By.CSS_SELECTOR, "[data-id='team-manage-invite-to-operator']")
    
    def waiter(self):
        self._wait_elements_displayed([self.INVITE_MANAGER_BTN])
        return self

    def verify_page(self):
        self._wait_elements_displayed([self.TEAM_MANAGEMENT_FORM_HEADER, self.DOCUMENT_FORM_HEADER, self.DOCUMENT_FORM])
        self._wait_elements_displayed([self.ACTIVITY_MANAGEMENT_HEADER, self.DECLINE_BTN, self.ACTIVITY_MANAGEMENT_FOOTER, self.ROLE_MANAGEMENT_HEADER, self.INVITE_MANAGER_BTN, self.INVITE_EMPLOYEE_BTN])
        asserts.soft_assert_equal(self._get_element_text(self.DECLINE_BTN), constants.REJECT)
        asserts.soft_assert_equal(self._get_element_text(self.INVITE_MANAGER_BTN), constants.INVITE_MANAGER_BTN)
        asserts.soft_assert_equal(self._get_element_text(self.INVITE_EMPLOYEE_BTN), constants.INVITE_EMPLOYEE_BTN)
        return self

    def click_manager_btn(self):
        self._click_element(self.INVITE_MANAGER_BTN)
        return self

    def click_employee_btn(self):
        self._click_element(self.INVITE_EMPLOYEE_BTN)
        return self

    def click_decline_btn(self):
        self._click_element(self.DECLINE_BTN)
        return self
