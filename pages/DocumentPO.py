from selenium.webdriver.common.by import By
from . import logger, asserts, constants
from pages.BasePO import BasePO

class DocumentPO(BasePO):
    SEND_TO_VALIDATION_BTN = (By.XPATH, f"//*[text()='{constants.SEND_TO_VALIDATION_BTN}']")
    SEND_TO_VALIDATION_BTN_ENG = (By.XPATH, f"//*[text()='{constants.SEND_TO_VALIDATION_BTN_ENG}']")

    def waiter(self):
        # TODO: find unique locator
        return self
    
    def verify_page(self, document_type, data_set):
        if document_type == constants.RF_PASSPORT:
            self.verify_passport(data_set)
        return self

    def verify_passport(self, data_set):
        # TODO: find a way to check gender
        self._verify_element_with_text(constants.RF_PASSPORT)
        for key in data_set:
            locator = (By.XPATH, f"//*[text()='{key}']//following-sibling::div//descendant::label//descendant::input[@value='{data_set[key]}']")
            self._wait_element_displayed(locator)

    def click_send_to_validation(self):
        self._click_element(self.SEND_TO_VALIDATION_BTN)