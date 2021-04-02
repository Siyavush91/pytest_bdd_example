from selenium.webdriver.common.by import By
from . import logger, asserts, constants
from pages.BasePO import BasePO

class CreateSubdomainPO(BasePO):
    TEMPLATES_TAB = (By.XPATH, f"//*[text()='{constants.TEMPLATES_TAB}']")
    REQUIREMENTS_TAB = (By.XPATH, f"//*[text()='{constants.REQUIREMENTS_TAB}']")
    REWARDS_TAB = (By.XPATH, f"//*[text()='{constants.REWARDS_TAB}']")

    CREATE_DOMAIN_HEADER = (By.XPATH, f"//*[text()='{constants.TEMPLATES_TAB}']")
    DOMAIN_NAME_LABEL = (By.XPATH, f"//*[text()='{constants.DOMAIN_NAME_LABEL}']")
    DOMAIN_NAME_INPUT = (By.XPATH, f"//*[text()='{constants.DOMAIN_NAME_LABEL}']//following-sibling::div//child::input")
    COUNTRY_CODE_LABEL = (By.XPATH, f"//*[text()='{constants.COUNTRY_CODE_LABEL}']")
    COUNTRY_CODE_INPUT = (By.XPATH, f"//*[text()='{constants.COUNTRY_CODE_LABEL}']//following-sibling::div//child::input")
    DOMAIN_AGREE_TICK = (By.CSS_SELECTOR, "[data-id='domain-agree-create-btn']")
    DOMAIN_AGREE_TICK_LABEL = (By.XPATH, f"//*[@data-id='domain-agree-create-btn']//child::span")
    DOMAIN_CREATE_BTN = (By.CSS_SELECTOR, "[data-id='domain-create-btn']")

    def waiter(self):
        self._wait_element_displayed(self.DOMAIN_AGREE_TICK)
        return self
    
    def verify_page(self):
        self._wait_elements_displayed([self.TEMPLATES_TAB, self.REQUIREMENTS_TAB, self.REWARDS_TAB])
        self._wait_elements_displayed([self.DOMAIN_NAME_LABEL, self.DOMAIN_NAME_INPUT, self.COUNTRY_CODE_LABEL, self.COUNTRY_CODE_INPUT])
        asserts.soft_assert_equal(self._get_placeholder_text(self.DOMAIN_NAME_INPUT), constants.DOMAIN_NAME_INPUT_PLACEHOLDER)
        asserts.soft_assert_equal(self._get_placeholder_text(self.COUNTRY_CODE_INPUT), constants.COUNTRY_CODE_INPUT_PLACEHOLDER)
        self._wait_elements_displayed([self.DOMAIN_AGREE_TICK, self.DOMAIN_CREATE_BTN])
        asserts.soft_assert_equal(self._get_element_text(self.DOMAIN_AGREE_TICK_LABEL), constants.DOMAIN_AGREE_TICK_LABEL)
        asserts.soft_assert_equal(self._get_element_text(self.DOMAIN_CREATE_BTN), constants.CREATE_BTN)
        return self

    def fill_domain_name(self, name):
        self.driver.find_element(*self.DOMAIN_NAME_INPUT).send_keys(name)

    def fill_country_code(self, value):
        self.driver.find_element(*self.COUNTRY_CODE_INPUT).send_keys(value)

    def accept_rules(self):
        self._click_element(self.DOMAIN_AGREE_TICK)

    def tap_create_btn(self):
        self._click_element(self.DOMAIN_CREATE_BTN)