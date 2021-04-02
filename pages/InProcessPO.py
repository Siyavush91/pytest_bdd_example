from selenium.webdriver.common.by import By
from . import logger, asserts, constants
from pages.BasePO import BasePO
from datetime import date

class InProcessPO(BasePO):
    CHECKED_DOCS_TAB = (By.XPATH, f"//*[text()='{constants.CHECKED_DOCS_TAB}']")
    COMPANY_DOCS_TAB = (By.XPATH, f"//*[text()='{constants.COMPANY_DOCS_TAB}']")
    IN_PROGRESS_DOCS_TAB = (By.XPATH, f"//*[text()='{constants.IN_PROGRESS_DOCS_TAB}']")
    ADD_DOCUMENT_BTN = (By.XPATH, f"//*[text()='{constants.ADD_DOCUMENT_BTN}']")
    SUSPENDED_SWITCHER = (By.XPATH, f"//*[text()='{constants.SUSPENDED_SWITCHER}']")
    WAITING_SWITCHER = (By.XPATH, f"//*[text()='{constants.WAITING_SWITCHER}']")

    TYPE_OF_DOC_HEADER = (By.XPATH, f"//*[text()='{constants.TYPE_OF_DOC_HEADER}']")
    STATUS_HEADER = (By.XPATH, f"//*[text()='{constants.STATUS_HEADER}']")
    DATE_HEADER = (By.XPATH, f"//*[text()='{constants.DATE_HEADER}']")

    # COMPANY_DOCS_TAB = (By.XPATH, f"//*[text()='{constants.COMPANY_DOCS_TAB}']")
    # IN_PROGRESS_DOCS_TAB = (By.XPATH, f"//*[text()='{constants.IN_PROGRESS_DOCS_TAB}']")
    # ADD_DOCUMENT_BTN = (By.XPATH, f"//*[text()='{constants.ADD_DOCUMENT_BTN}']")
    # TYPE_OF_DOC_HEADER = (By.XPATH, f"//*[text()='{constants.TYPE_OF_DOC_HEADER}']")
    VERIFICATION_TYPE_HEADER = (By.XPATH, f"//*[text()='{constants.TYPE_OF_VERIFICATION_HEADER}']")
    # DATE_HEADER = (By.XPATH, f"//*[text()='{constants.DATE_HEADER}']")

    COMPANY_DOCS_TAB_ENG = (By.XPATH, f"//*[text()='{constants.COMPANY_DOCS_TAB_ENG}']")
    IN_PROGRESS_DOCS_TAB_ENG = (By.XPATH, f"//*[text()='{constants.IN_PROGRESS_DOCS_TAB_ENG}']")
    ADD_DOCUMENT_BTN_ENG = (By.XPATH, f"//*[text()='{constants.ADD_DOCUMENT_BTN_ENG}']")
    TYPE_OF_DOC_HEADER_ENG = (By.XPATH, f"//*[text()='{constants.TYPE_OF_DOC_HEADER_ENG}']")
    VERIFICATION_TYPE_HEADER_ENG = (By.XPATH, f"//*[text()='{constants.TYPE_OF_VERIFICATION_HEADER_ENG}']")
    DATE_HEADER_ENG = (By.XPATH, f"//*[text()='{constants.DATE_HEADER_ENG}']")

    def waiter(self):
        # locator = (By.XPATH, f"//*[text()='{constants.IN_PROGRESS_DOCS_TAB}']//parent::div")
        # self._wait_element_active(locator)
        self._wait_element_displayed(self.IN_PROGRESS_DOCS_TAB)
        return self
    
    def verify_page(self):
        # locator = (By.XPATH, f"//*[text()='{constants.IN_PROGRESS_DOCS_TAB}']//parent::div")
        # self._wait_element_active(locator)
        self._wait_elements_displayed([self.COMPANY_DOCS_TAB, self.IN_PROGRESS_DOCS_TAB, self.SUSPENDED_SWITCHER, self.WAITING_SWITCHER])
        self._wait_elements_displayed([self.ADD_DOCUMENT_BTN, self.TYPE_OF_DOC_HEADER, self.STATUS_HEADER, self.VERIFICATION_TYPE_HEADER, self.DATE_HEADER])
        return self

    def verify_doc(self, name, status, verification_colour, verification_type):
        self._verify_element_with_text(name)
        locator = (By.XPATH, f"//div[text()='{name}']//following-sibling::div[text()='{status}']//following-sibling::div//descendant::div[text()='{verification_type}'][@color='{verification_colour}']")
        self._wait_element_displayed(locator)
        self._verify_element_contains_text(date.today().strftime("%d.%m"))

    def click_on_doc(self, name):
        locator = (By.XPATH, f"//*[text()='{name}']")
        self._click_element(locator)
