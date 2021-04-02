from selenium.webdriver.common.by import By
from . import logger, asserts, constants
from pages.BasePO import BasePO

class VerificationTypeSelectionPO(BasePO):
    VERIFICATION_TYPE_HEADER = (By.XPATH, f"//*[text()='{constants.VERIFICATION_TYPE_HEADER}']")
    GLOBAL_HEADER = (By.XPATH, f"//*[text()='{constants.GLOBAL_HEADER}']")
    LOCAL_HEADER = (By.XPATH, f"//*[text()='{constants.LOCAL_HEADER}']")
    GLOBAL_DOC_DESC = (By.XPATH, f"//*[text()='{constants.GLOBAL_DOC_DESC}']")
    LOCAL_DOC_DESC = (By.XPATH, f"//*[text()='{constants.LOCAL_DOC_DESC}']")
    GLOBAL_GREEN_DESC = (By.XPATH, f"//*[text()='{constants.GLOBAL_GREEN_DESC}']")
    GLOBAL_YELLOW_DESC = (By.XPATH, f"//*[text()='{constants.GLOBAL_YELLOW_DESC}']")
    LOCAL_GREEN_DESC = (By.XPATH, f"//*[text()='{constants.LOCAL_GREEN_DESC}']")
    LOCAL_YELLOW_DESC = (By.XPATH, f"//*[text()='{constants.LOCAL_YELLOW_DESC}']")
    GREEN_CHOOSE_BTN = (By.XPATH, f"//*[text()='{constants.GREEN_CHOOSE_BTN}']")
    YELLOW_CHOOSE_BTN = (By.XPATH, f"//*[text()='{constants.YELLOW_CHOOSE_BTN}']")
    DETAILS_BTN = (By.XPATH, f"//*[text()='{constants.DETAILS_BTN}']")

    def waiter(self):
        # TODO: find unique locator
        return self
    
    def verify_page(self):
        self._wait_elements_displayed([self.VERIFICATION_TYPE_HEADER, self.GLOBAL_HEADER, self.LOCAL_HEADER])
        self._wait_elements_displayed([self.GLOBAL_DOC_DESC, self.LOCAL_DOC_DESC, self.GLOBAL_GREEN_DESC, self.GLOBAL_YELLOW_DESC])
        self._wait_elements_displayed([self.LOCAL_GREEN_DESC, self.LOCAL_YELLOW_DESC, self.GREEN_CHOOSE_BTN, self.YELLOW_CHOOSE_BTN, self.DETAILS_BTN])
        return self

    def click_green_global(self):
        self._click_element(self.GREEN_CHOOSE_BTN)