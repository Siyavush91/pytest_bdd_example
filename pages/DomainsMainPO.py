from selenium.webdriver.common.by import By

from . import logger, asserts, constants
from pages.BasePO import BasePO

class DomainsMainPO(BasePO):
    TEMPLATES_TAB = (By.XPATH, f"//*[text()='{constants.TEMPLATES_TAB}']")
    REQUIREMENTS_TAB = (By.XPATH, f"//*[text()='{constants.REQUIREMENTS_TAB}']")
    REWARDS_TAB = (By.XPATH, f"//*[text()='{constants.REWARDS_TAB}']")
    DOMAINS_HEADER = (By.XPATH, f"//*[text()='{constants.DOMAINS_HEADER}']")
    MH_GLOBAL_PANEL = (By.XPATH, f"//*[text()='{constants.MH_GLOBAL_PANEL}']")
    RF_PANEL = (By.XPATH, f"//*[text()='{constants.RF_PANEL}']")
    TEMPLATES_NUMBER = (By.XPATH, f"//*[text()='{constants.TEMPLATES_NUMBER}']")
    SUBDOMAINS_NUMBER = (By.XPATH, f"//*[text()='{constants.SUBDOMAINS_NUMBER}']")
    CREATE_DOMAIN_BTN = (By.XPATH, f"//*[text()='{constants.CREATE_DOMAIN_BTN}']")

    def verify_page(self):
        self._wait_elements_displayed([self.TEMPLATES_TAB, self.REQUIREMENTS_TAB, self.REWARDS_TAB])
        self._wait_elements_displayed([self.DOMAINS_HEADER, self.CREATE_DOMAIN_BTN, self.MH_GLOBAL_PANEL, self.RF_PANEL])
        self._wait_elements_displayed([self.TEMPLATES_NUMBER, self.SUBDOMAINS_NUMBER])
        return self

    def open_mh_global(self):
        self._click_element(self.MH_GLOBAL_PANEL)
        return self

    def open_rf_domain(self):
        self._click_element(self.RF_PANEL)
        return self

    def click_create_domain(self):
        self._click_element(self.CREATE_DOMAIN_BTN)
        return self

    def go_to_requirements(self):
        self._click_element(self.REQUIREMENTS_TAB)
        return self
