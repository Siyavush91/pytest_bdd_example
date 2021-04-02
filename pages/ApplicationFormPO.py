from selenium.webdriver.common.by import By
from helpers import constants
from pages.BasePO import BasePO
import allure


class ApplicationFormPO(BasePO):
    """Содержит методы для взаимодействия с элементами страницы 'Анкета с заявкой'"""

    # КНОПКИ ФОРМЫ

    CHECKBOX = (By.CSS_SELECTOR, "[data-id='approve-rules-checkbox'] > div")
    ACCEPT_BTN = (By.CSS_SELECTOR, "[data-id='approve-button']")

    SUSPEND_BTN = (By.CSS_SELECTOR, "[data-id='suspend-button']")
    DECLINE_BTN = (By.CSS_SELECTOR, "[data-id='decline-button']")

    # ЧАТ
    CHAT_SEND_BTN = (By.CSS_SELECTOR, "div.chat__footer > a")
    INSERT_MSG_FIELD = (By.CSS_SELECTOR, "textarea")

    # ПОПАП С КОММЕНТАРИЕМ
    POPUP_TEXT_FIELD = (By.CSS_SELECTOR, "[data-id='decline-application-input']")
    POPUP_SEND_BTN = (By.CSS_SELECTOR, "[data-id='decline-application-button']")

    def verify_document(self):
        self._wait_elements_displayed([self.DECLINE_BTN, self.ACCEPT_BTN])
        actual_reject_btn = self._get_element_text(self.DECLINE_BTN)
        actual_accept_btn = self._get_element_text(self.ACCEPT_BTN)
        assert actual_reject_btn == constants.REJECT
        assert actual_accept_btn == constants.ACCEPT
        return


    def click_agree_checkbox(self):
        """
        Клик по кнопке "Запросить заявку"
        """
        with allure.step(f"Поставить галочку чек-бокс 'Запросить заявку' {self.CHECKBOX}"):
            self._click_element(self.CHECKBOX)
            return self


    def click_accept_button(self):
        """
        Клик по кнопке "Подписать" в заявке
        """
        with allure.step(f"Клик по кнопке 'Подписать' {self.ACCEPT_BTN}"):
            self._click_element(self.ACCEPT_BTN)
            return self

    def click_suspend_button(self):
        """
        Клик по кнопке "Приостановить" в заявке
        :return:
        """
        self._click_element(self.SUSPEND_BTN)
        return self


    def click_decline_button(self):
        """
        Клик по кнопке "Отклонить" в заявке
        :return:
        """
        with allure.step(f"Клик по кнопке 'Отклонить' {self.DECLINE_BTN}"):
            self._click_element(self.DECLINE_BTN)
            return self

    def verify_popup(self):
        self._wait_for_element_present(self.POPUP_SEND_BTN)
        return self

    def fill_decline_comment_popup(self, comments):
        """
        Заполнить попап для комментария и кликнуть "Отправить"
        """
        with allure.step(f"Ввести в поле {self.POPUP_TEXT_FIELD} текст"):
            self.driver.find_element(*self.POPUP_TEXT_FIELD).send_keys(comments)
        with allure.step(f"Клик по кнопке 'Отправить' {self.POPUP_SEND_BTN}"):
            self._click_element(self.POPUP_SEND_BTN)
            return self
