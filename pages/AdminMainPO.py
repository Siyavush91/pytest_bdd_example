from selenium.webdriver.common.by import By
from pages.BasePO import BasePO
from . import logger, asserts, constants
from modules import header_module, side_menu_module
import re, time


class AdminMainPO(BasePO):
    """Содержит методы для взаимодействия с элементами страницы 'Главная' """

    COUNT_BANNER_TITLE = (By.CLASS_NAME, "count-banner__title")
    COUNT_BANNER_VALUE = (By.CLASS_NAME, "count-banner__value")
    PROCESS_VERIFICATION_BTN = (By.CSS_SELECTOR, "[data-id='process-verification-button']")
    LINK_FOR_CLIENTS = (By.XPATH, "//*[text()='Ссылка для ваших клиентов']")
    WORK_RULES = (By.XPATH, "//*[text()='Правила работы']")
    REPORT_FLOW_TABS = (By.CLASS_NAME, "report-flow__tabs") 
    MY_WALLET_TAB = (By.XPATH, "//*[text()='Личный кошелек']")
    COMPANY_WALLET_TAB = (By.XPATH, "//*[text()='Кошелек компании']")
    OUTPUT_BTN = (By.CLASS_NAME, "wallet-details__scores__header__left-block")
    WALLET_SCORES_TITLE = (By.CLASS_NAME, "wallet-details__scores__header__score-block__title")
    WALLET_SCORES_COUNT = (By.CLASS_NAME, "wallet-details__scores__header__score-block__count") 
    WALLET_SCORES_ANOTHER_CURRENCY = (By.CLASS_NAME, "wallet-details__scores__header__score-block__another-currency-rate")
    INPUT_BUTTON = (By.CLASS_NAME, "wallet-details__scores__header__right-block")
    DATE_RANGE_LABEL = (By.CLASS_NAME, "date-range__date-picker-part__label")
    DATE_RANGE_INPUT = (By.CLASS_NAME, "date-range__input-container__input")
    DATE_RANGE_CALENDAR = (By.CLASS_NAME, "date-range__input-container__calendar")
    DATE_RANGE_BTN = (By.CLASS_NAME, "date-range__button")
    PROGRESS_BAR = (By.CLASS_NAME, "preloader-cap__icon")

    def goto_application(self):
        self._click_element(self.PROCESS_VERIFICATION_BTN)
        return self

    def waiter(self):
        self.wait_loader_not_displayed()
        self._wait_for_elements_present([self.COUNT_BANNER_TITLE, self.OUTPUT_BTN, self.DATE_RANGE_BTN])
        return self

    def verify_screen(self):
        self._wait_for_elements_present([self.COUNT_BANNER_TITLE, self.COUNT_BANNER_VALUE, self.PROCESS_VERIFICATION_BTN])
        self._wait_for_elements_present([self.REPORT_FLOW_TABS, self.OUTPUT_BTN])
        self._wait_for_elements_present([self.WALLET_SCORES_TITLE, self.WALLET_SCORES_COUNT, self.WALLET_SCORES_ANOTHER_CURRENCY, self.INPUT_BUTTON])
        self._wait_for_elements_present([self.DATE_RANGE_LABEL, self.DATE_RANGE_INPUT, self.DATE_RANGE_CALENDAR, self.DATE_RANGE_BTN])

        asserts.soft_assert_equal(self._get_element_texts(self.COUNT_BANNER_TITLE)[0], constants.COUNT_BANNER_TITLE1)
        asserts.soft_assert_equal(self._get_element_texts(self.COUNT_BANNER_TITLE)[1], constants.COUNT_BANNER_TITLE2)
        asserts.soft_assert_equal(self._get_element_texts(self.COUNT_BANNER_TITLE)[2], constants.COUNT_BANNER_TITLE3)
        asserts.soft_assert_equal(self._get_element_text(self.PROCESS_VERIFICATION_BTN), constants.PROCESS_VERIFICATION_BTN)

        self._wait_for_elements_present([self.LINK_FOR_CLIENTS, self.WORK_RULES])
        self._wait_for_elements_present([self.MY_WALLET_TAB, self.COMPANY_WALLET_TAB])
        asserts.soft_assert_equal(self._get_element_text(self.OUTPUT_BTN), constants.OUTPUT_BTN)
        asserts.soft_assert_equal(self._get_element_text(self.WALLET_SCORES_TITLE), constants.WALLET_SCORES_TITLE)
        asserts.soft_assert_equal(self._get_element_text(self.INPUT_BUTTON), constants.INPUT_BUTTON)

        asserts.assert_is_not_none(re.match(r'^.+ETH$', self._get_element_text(self.WALLET_SCORES_COUNT)))
        asserts.assert_is_not_none(re.match(r'^.+USD$', self._get_element_text(self.WALLET_SCORES_ANOTHER_CURRENCY)))

        asserts.soft_assert_equal(self._get_element_texts(self.DATE_RANGE_LABEL)[0], constants.DATE_RANGE_LABEL_SINCE)
        asserts.soft_assert_equal(self._get_element_texts(self.DATE_RANGE_LABEL)[1], constants.DATE_RANGE_LABEL_UNTIL)
        asserts.soft_assert_equal(self._get_element_text(self.DATE_RANGE_BTN), constants.DATE_RANGE_BTN)
        header_module.verify_header(self)
        side_menu_module.verify_work_side_menu(self)

    def wait_loader_not_displayed(self):
        self._wait_for_element_not_present(self.PROGRESS_BAR)
        time.sleep(0.5)
        return self

