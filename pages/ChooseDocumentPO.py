from selenium.webdriver.common.by import By
from . import logger, asserts, constants
from pages.BasePO import BasePO

class ChooseDocumentPO(BasePO):
    CHOOSE_DOCUMENT_HEADER = (By.XPATH, f"//*[text()='{constants.CHOOSE_DOCUMENT_HEADER}']")

    def waiter(self):
        self._wait_element_displayed(self.CHOOSE_DOCUMENT_HEADER)
        return self

    def choose_domain(self, domain):
        locator = (By.XPATH, f"//*[text()='{domain}']")
        self._click_element(locator)

    def verify_document(self, document):
        self._verify_element_with_text(document)

    def choose_document(self, document):
        locator = (By.XPATH, f"//*[text()='{document}']")
        self._click_element(locator)
