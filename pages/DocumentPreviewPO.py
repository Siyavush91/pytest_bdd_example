from selenium.webdriver.common.by import By
from . import logger, asserts, constants
from pages.BasePO import BasePO

class DocumentPreviewPO(BasePO):
    DOC_PREVIEW_HEADER = (By.XPATH, f"//*[text()='{constants.DOC_PREVIEW_HEADER}']")
    DOC_NAME_LABEL = (By.XPATH, f"//*[text()='{constants.DOC_NAME_LABEL}']")
    VERIFICATION_TYPE_LABEL = (By.XPATH, f"//*[text()='{constants.VERIFICATION_TYPE_LABEL}']")
    SEND_TO_VALIDATOR_BTN = (By.XPATH, f"//*[text()='{constants.SEND_TO_VALIDATOR_BTN}']")
    ENCRYPT_TO_VALIDATOR_BTN = (By.XPATH, f"//*[text()='{constants.ENCRYPT_TO_VALIDATOR_BTN}']")
    REFUSE_VALIDATION_BTN = (By.XPATH, f"//*[text()='{constants.REFUSE_VALIDATION_BTN}']")

    def waiter(self):
        # TODO: find unique locator
        return self
    
    def verify_page(self, document_type, data_set, check_header):
        if check_header:
            self._wait_element_displayed(self.DOC_PREVIEW_HEADER)
        self._wait_elements_displayed([self.DOC_NAME_LABEL, self.VERIFICATION_TYPE_LABEL])
        if document_type == constants.RF_PASSPORT:
            self.verify_passport(data_set)
        return self

    def verify_passport(self, data_set):
        # TODO: find a way to check gender
        self._verify_element_with_text(constants.RF_PASSPORT)
        for key in data_set:
            locator = (By.XPATH, f"//*[text()='{key}']//following-sibling::div//descendant::label//descendant::input[@value='{data_set[key]}']")
            self._wait_element_displayed(locator)

    def verify_global_green_verification(self):
        self._verify_element_with_text(constants.GLOBAL_HEADER)
        locator = (By.XPATH, f"//*[text()='{constants.GLOBAL_HEADER}']//descendant::div[@color='GRN']")
        self._wait_element_displayed(locator)

    def verify_send_to_validator_button(self):
        self._wait_element_displayed(self.SEND_TO_VALIDATOR_BTN)
    
    def verify_encrypt_buttons(self):
        self._wait_elements_displayed([self.ENCRYPT_TO_VALIDATOR_BTN, self.REFUSE_VALIDATION_BTN])

    def verify_no_encrypt_buttons(self):
        self._wait_for_elements_not_present([self.ENCRYPT_TO_VALIDATOR_BTN, self.REFUSE_VALIDATION_BTN])

    def click_send_to_validator(self):
        self._click_element(self.SEND_TO_VALIDATOR_BTN)

    def click_encrypt_to_validator(self):
        self._click_element(self.ENCRYPT_TO_VALIDATOR_BTN)