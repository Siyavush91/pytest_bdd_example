from selenium.webdriver.common.by import By
from . import logger, asserts, constants
from pages.BasePO import BasePO

class RequirementsMainPO(BasePO):
    TEMPLATES_TAB = (By.XPATH, f"//*[text()='{constants.TEMPLATES_TAB}']")
    REQUIREMENTS_TAB = (By.XPATH, f"//*[text()='{constants.REQUIREMENTS_TAB}']")
    REWARDS_TAB = (By.XPATH, f"//*[text()='{constants.REWARDS_TAB}']")

    REQUIREMENTS_HEADER = (By.XPATH, f"//*[text()='{constants.REQUIREMENTS_HEADER}']")
    CREATE_REQUIREMENT_BTN = (By.XPATH, f"//*[text()='{constants.CREATE_REQUIREMENT_BTN}']")
    REQUIREMENTS_TABLE_HEADER = (By.XPATH, f"//*[text()='{constants.REQUIREMENTS_TABLE_HEADER}']")
    REQUIREMENTS_TABLE_DOMAIN = (By.XPATH, f"//*[text()='{constants.REQUIREMENTS_TABLE_DOMAIN}']")
    REQUIREMENTS_TABLE_TYPE = (By.XPATH, f"//*[text()='{constants.REQUIREMENTS_TABLE_TYPE}']")

    def waiter(self):
        self._wait_element_displayed(self.CREATE_REQUIREMENT_BTN)
        return self

    def verify_page(self):
        self._wait_elements_displayed([self.TEMPLATES_TAB, self.REQUIREMENTS_TAB, self.REWARDS_TAB])
        self._wait_elements_displayed([self.REQUIREMENTS_HEADER, self.CREATE_REQUIREMENT_BTN])
        self._wait_elements_displayed([self.REQUIREMENTS_TABLE_HEADER, self.REQUIREMENTS_TABLE_DOMAIN, self.REQUIREMENTS_TABLE_TYPE])
        self.verify_four_base_requirements()
        return self

    def verify_four_base_requirements(self):
        local_green_name = (By.XPATH, f"//*[text()='{constants.LOCAL_DOC_DESC}']")
        local_green_domain = (By.XPATH, f"//*[text()='{constants.LOCAL_DOC_DESC}']//parent::td//following-sibling::td//child::div[text()='{constants.MH_GLOBAL_PANEL}']")
        local_green_type = (By.XPATH, f"//*[text()='{constants.LOCAL_DOC_DESC}']//parent::td//following-sibling::td//following-sibling::td//child::div[text()='{constants.LOCAL_GREEN_TYPE}']")
        global_yellow_name = (By.XPATH, f"//*[text()='{constants.GLOBAL_DOC_DESC}']")
        global_yellow_domain = (By.XPATH, f"//*[text()='{constants.GLOBAL_DOC_DESC}']//parent::td//following-sibling::td//child::div[text()='{constants.MH_GLOBAL_PANEL}']")
        global_yellow_type = (By.XPATH, f"//*[text()='{constants.GLOBAL_DOC_DESC}']//parent::td//following-sibling::td//following-sibling::td//child::div[text()='{constants.GLOBAL_YELLOW_TYPE}']")
        global_green_name = (By.XPATH, f"//*[text()='{constants.GLOBAL_DOC_DESC}']")
        global_green_domain = (By.XPATH, f"//*[text()='{constants.GLOBAL_DOC_DESC}']//parent::td//following-sibling::td//child::div[text()='{constants.MH_GLOBAL_PANEL}']")
        global_green_type = (By.XPATH, f"//*[text()='{constants.GLOBAL_DOC_DESC}']//parent::td//following-sibling::td//following-sibling::td//child::div[text()='{constants.GLOBAL_GREEN_TYPE}']")
        local_yellow_name = (By.XPATH, f"//*[text()='{constants.LOCAL_DOC_DESC}']")
        local_yellow_domain = (By.XPATH, f"//*[text()='{constants.LOCAL_DOC_DESC}']//parent::td//following-sibling::td//child::div[text()='{constants.MH_GLOBAL_PANEL}']")
        local_yellow_type = (By.XPATH, f"//*[text()='{constants.LOCAL_DOC_DESC}']//parent::td//following-sibling::td//following-sibling::td//child::div[text()='{constants.LOCAL_YELLOW_TYPE}']")
        self._wait_elements_displayed([local_green_name, local_green_domain, local_green_type])
        self._wait_elements_displayed([global_yellow_name, global_yellow_domain, global_yellow_type])
        self._wait_elements_displayed([global_green_name, global_green_domain, global_green_type])
        self._wait_elements_displayed([local_yellow_name, local_yellow_domain, local_yellow_type])

    def verify_added_requirement(self, req_name, req_domain, req_type):
        name_loc = (By.XPATH, f"//*[text()='{req_name}']")
        domain_loc = (By.XPATH, f"//*[text()='{req_name}']//parent::td//following-sibling::td//child::div[text()='{req_domain}']")
        type_loc = (By.XPATH, f"//*[text()='{req_name}']//parent::td//following-sibling::td//following-sibling::td//child::div[text()='{req_type}']")
        self._wait_elements_displayed([name_loc, domain_loc, type_loc])

    def click_requirement(self, req):
        locator = (By.XPATH, f"//*[text()='{req}']")
        self._click_element(locator)

    def go_to_create_requirement(self):
        self._click_element(self.CREATE_REQUIREMENT_BTN)
