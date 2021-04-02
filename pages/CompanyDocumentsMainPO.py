from selenium.webdriver.common.by import By
from . import logger, asserts, constants
from pages.BasePO import BasePO
from datetime import date
import time

class CompanyDocumentsMainPO(BasePO):
    CHECKED_DOCS_TAB = (By.XPATH, f"//*[text()='{constants.CHECKED_DOCS_TAB}']")
    COMPANY_DOCS_TAB = (By.CSS_SELECTOR, "a.panel-tabs__StyledPanelTab-s1sr90-3.gCBCTY")
    IN_PROGRESS_DOCS_TAB = (By.XPATH, f"//*[text()='{constants.IN_PROGRESS_DOCS_TAB}']")
    ADD_DOCUMENT_BTN = (By.XPATH, f"//*[text()='{constants.ADD_DOCUMENT_BTN}']")
    TYPE_OF_DOC_HEADER = (By.XPATH, f"//*[text()='{constants.TYPE_OF_DOC_HEADER}']")
    VERIFICATION_TYPE_HEADER = (By.XPATH, f"//*[text()='{constants.TYPE_OF_VERIFICATION_HEADER}']")
    DATE_HEADER = (By.XPATH, f"//*[text()='{constants.DATE_HEADER}']")

    COMPANY_DOCS_TAB_ENG = (By.XPATH, f"//*[text()='{constants.COMPANY_DOCS_TAB_ENG}']")
    IN_PROGRESS_DOCS_TAB_ENG = (By.XPATH, f"//*[text()='{constants.IN_PROGRESS_DOCS_TAB_ENG}']")
    ADD_DOCUMENT_BTN_ENG = (By.XPATH, f"//*[text()='{constants.ADD_DOCUMENT_BTN_ENG}']")
    TYPE_OF_DOC_HEADER_ENG = (By.XPATH, f"//*[text()='{constants.TYPE_OF_DOC_HEADER_ENG}']")
    VERIFICATION_TYPE_HEADER_ENG = (By.XPATH, f"//*[text()='{constants.TYPE_OF_VERIFICATION_HEADER_ENG}']")
    DATE_HEADER_ENG = (By.XPATH, f"//*[text()='{constants.DATE_HEADER_ENG}']")
    PROGRESS_BAR = (By.CLASS_NAME, "preloader-cap__icon")

    def waiter(self):
        self.wait_loader_not_displayed()
        self._wait_element_active(self.COMPANY_DOCS_TAB)
        # self._wait_element_displayed(self.COMPANY_DOCS_TAB)
        return self
    
    def verify_page(self):
        # locator = (By.XPATH, "//*[text()='Документы компании']"[1])
        self._wait_element_active(self.COMPANY_DOCS_TAB)
        self._wait_elements_displayed([self.COMPANY_DOCS_TAB, self.IN_PROGRESS_DOCS_TAB])
        self._wait_elements_displayed([self.ADD_DOCUMENT_BTN, self.TYPE_OF_DOC_HEADER, self.VERIFICATION_TYPE_HEADER, self.DATE_HEADER])
        return self

    def verify_doc(self, name):
        self._verify_element_with_text(name)
        self._verify_element_contains_text(date.today().strftime("%d.%m"))

    def verify_no_doc(self, name):
        self._verify_no_element_with_text(name)

    def click_on_doc(self, name):
        locator = (By.XPATH, f"//*[text()='{name}']")
        self._click_element(locator)

    def click_add_doc(self):
        self._click_element(self.ADD_DOCUMENT_BTN)
        return self

    def open_in_progress_tab(self):
        self._click_element(self.IN_PROGRESS_DOCS_TAB)

    def wait_loader_not_displayed(self):
        self._wait_for_element_not_present(self.PROGRESS_BAR)
        time.sleep(0.5)
        return self
