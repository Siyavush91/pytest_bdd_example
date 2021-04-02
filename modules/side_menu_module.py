from selenium.webdriver.common.by import By
from pages.ApplicationPO import ApplicationPO
from pages.BasePO import BasePO
from . import logger, asserts, constants

AVATAR = (By.CSS_SELECTOR, "div.avatar-block__Container-sc-1czor0t-0.iWVnHj") #TODO rebase after add data-id
COMPANY_SELECTOR = (By.CSS_SELECTOR, "div.company-selection__Container-sc-14zgnv6-0.eGEKXk.sidebar__StyledCompanySelection-sc-1y25585-1.bAQJbf") #TODO rebase after add data-id
MENU_ADMIN_SWITCHER = (By.CSS_SELECTOR, "[data-id='admin']")
NAVIGATION_MENU = (By.CSS_SELECTOR, "[data-id='navigation-menu']")
# TODO: can't check main button and icons for side menu

HOME_PAGE = (By.CSS_SELECTOR, "[data-id='home-page']")
APPLICATIONS = (By.CSS_SELECTOR, "[data-id='applications']")
ISSUED_LICENSES = (By.CSS_SELECTOR, "[data-id='issued-licenses']")
REFERRALS = (By.CSS_SELECTOR, "[data-id='refferals']")

TEAM_MANAGEMENT = (By.CSS_SELECTOR, "[data-id='team-management']")
PARTNERS = (By.CSS_SELECTOR, "[data-id='partners']")
COMPANY_MANAGEMENT = (By.CSS_SELECTOR, "[data-id='company-management']")
COMPANY_DOCUMENTS = (By.CSS_SELECTOR, "[data-id='company-documents']")
DOMAINS = (By.CSS_SELECTOR, "[data-id='domains']")
VALIDATORS = (By.CSS_SELECTOR, "[data-id='validators']")
SERVICE_REGULATORS = (By.CSS_SELECTOR, "[data-id='service-regulators']")
MENU_WORK_SWITCHER = (By.CSS_SELECTOR, "[data-id='work']")
# TODO: RUSWAN -- no locators

def side_menu_wait(self):
     self._wait_for_element_present(NAVIGATION_MENU)

def verify_default_side_menu(self):
    self._wait_for_elements_present([NAVIGATION_MENU, AVATAR])

def verify_work_side_menu(self):
    verify_default_side_menu(self)
    self._wait_for_elements_present([HOME_PAGE, APPLICATIONS, ISSUED_LICENSES, REFERRALS, MENU_ADMIN_SWITCHER])
    asserts.soft_assert_equal(self._get_element_text(HOME_PAGE), constants.HOME_PAGE)
    asserts.soft_assert_equal(self._get_element_text(APPLICATIONS), constants.APPLICATIONS)
    asserts.soft_assert_equal(self._get_element_text(ISSUED_LICENSES), constants.ISSUED_LICENSES)
    asserts.soft_assert_equal(self._get_element_text(REFERRALS), constants.REFERRALS)

def verify_admin_side_menu(self):
    verify_default_side_menu(self)
    self._wait_for_elements_present([TEAM_MANAGEMENT, PARTNERS, COMPANY_MANAGEMENT, DOMAINS, VALIDATORS, SERVICE_REGULATORS, MENU_WORK_SWITCHER])
    asserts.soft_assert_equal(self._get_element_text(TEAM_MANAGEMENT), constants.TEAM_MANAGEMENT)
    asserts.soft_assert_equal(self._get_element_text(PARTNERS), constants.PARTNERS)
    asserts.soft_assert_equal(self._get_element_text(COMPANY_MANAGEMENT), constants.COMPANY_MANAGEMENT)
    asserts.soft_assert_equal(self._get_element_text(COMPANY_DOCUMENTS), constants.COMPANY_DOCUMENTS)
    asserts.soft_assert_equal(self._get_element_text(DOMAINS), constants.DOMAINS)
    asserts.soft_assert_equal(self._get_element_texts(VALIDATORS)[0], constants.VALIDATORS_INVITE)
    asserts.soft_assert_equal(self._get_element_texts(VALIDATORS)[1], constants.VALIDATORS_ACCEPT)
    asserts.soft_assert_equal(self._get_element_text(SERVICE_REGULATORS), constants.SERVICE_REGULATORS)
