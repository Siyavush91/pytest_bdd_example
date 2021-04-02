import sys

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException, \
    StaleElementReferenceException
import time
from unittestzero import Assert
from selenium.webdriver.common.by import By
from . import asserts

"""
Base Page comes here.
"""
TIMEOUT=20
DRIVER_TIMEOUT = 1
POLL_FREQUENCY = 0.5

class BasePO:
    """
    Base класс для инициализации базовой страницы, которая будет вызываться всеми остальными страницами.
    """

    def __init__(self, driver = None):
        """
        Инициализация driver.

        """
        self.driver = driver
        self.driver.implicitly_wait(DRIVER_TIMEOUT)
        self.elements_name = {}


    def _is_element_visible(self, *selector):
        try:
            return self.driver.find_element(*selector).is_displayed()
        except (NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException):
            return False


    def _wait_to_be_selected(self, *selector):
        try:
            return WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(selector))
        except (NoSuchElementException, ElementNotVisibleException, TimeoutException):
            return False

    def _check_element_active(self, selector):
        try:
            self._wait_for_element_present(selector)
            return "active" in self._get_class(selector)
        except (NoSuchElementException, ElementNotVisibleException, TimeoutException):
            return False

    def _check_element_clickable(self, *selector):
        try:
            return WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(selector))
        except (NoSuchElementException, ElementNotVisibleException, TimeoutException):
            return False

    def _check_element_enable(self, *selector):
        try:
            return WebDriverWait(self.driver, TIMEOUT).until(EC.element_selection_state_to_be(self.driver.find_element(*selector), True))
        except (NoSuchElementException, ElementNotVisibleException, TimeoutException):
            return False

    def _wait_for_element_visible(self, *selector):
        count = 0
        element = self._is_element_visible(*selector)
        while not element:
            time.sleep(1)
            count += 1
            if count == TIMEOUT:
                raise Exception(':'.join(*selector) + " is not visible")
            else:
                return True

    def _wait_for_element_present(self, selector):
        """Wait for an element to become present."""
        try:
            WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located(selector))
        except TimeoutException:
            Assert.fail(TimeoutException)
        finally:
            # set back to where you once belonged
            self.driver.implicitly_wait(DRIVER_TIMEOUT)

    def _wait_for_elements_present(self, elements):
        for element in elements:
            self._wait_for_element_present(element)

    def _wait_for_element_not_present(self, selector):
        """Wait for an element to become not present."""
        try:
            WebDriverWait(self.driver, TIMEOUT).until(EC.invisibility_of_element_located(selector))
            # WebDriverWait(self.driver, timeout).until(lambda s: len(self.driver.find_elements(*selector)) < 1)
            return True
        except TimeoutException:
            Assert.fail(TimeoutException)

    def _wait_for_elements_not_present(self, elements):
        for element in elements:
            self._wait_for_element_not_present(element)

    def _wait_for_alert(self):
        return EC.alert_is_present

    def _is_element_not_visible(self, *selector):
        self.driver.implicitly_wait(DRIVER_TIMEOUT)
        try:
            return not self.driver.find_element(*selector).is_displayed()
        except (NoSuchElementException, ElementNotVisibleException):
            return True
        finally:
            # set back to where you once belonged
            self.driver.implicitly_wait(DRIVER_TIMEOUT)

    def _get_element_text(self, selector):
        e = "No text in element"
        try:
            text = self.driver.find_element(*selector).text
            return text
        except Exception as e:
            return e

    def _get_element_texts(self, selector):
        try:
            WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located(selector))
            self.elements = self.driver.find_elements(*selector)
            if self.elements == None:
                return None
            for i in range(self.elements.__len__()):
                element_name_tmp = self.elements[i].text
                if element_name_tmp != None:
                    self.elements_name[i] = element_name_tmp
                else:
                    sys.stdout.write("STDOUT: find search result name is null. \n")
            return self.elements_name
        except Exception as e:
            raise e

    def _get_placeholder_text(self, selector):
        e = "No placeholder in element"
        try:
            text = self.driver.find_element(*selector).get_attribute("placeholder")
            return text
        except Exception as e:
            return e

    def _get_class(self, selector):
        e = "No placeholder in element"
        try:
            class_name = self.driver.find_element(*selector).get_attribute("class")
            return class_name
        except Exception as e:
            return e

    def _is_element_enabled(self, *selector):
        return self.driver.find_element(*selector).is_enabled()


    def _wait_elements_displayed(self, selectors):
        for element in selectors:
            self._wait_element_displayed(element)

    def _wait_element_displayed(self, loc):
        try:
            WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located(loc))
        except TimeoutException:
            error_message = f" Can't find specific element, locator is {loc} "
            raise TimeoutException(error_message)

    def _wait_element_active(self, loc):
        end_time = time.time() + TIMEOUT
        while True:
            if self._check_element_active(loc):
                return True
            time.sleep(POLL_FREQUENCY)
            if time.time() > end_time:
                break
        raise TimeoutException(f"Element is not active")

    def _wait_element_clickable(self, loc):
        end_time = time.time() + TIMEOUT
        while True:
            if self._check_element_clickable(*loc):
                return True
            time.sleep(POLL_FREQUENCY)
            if time.time() > end_time:
                break
        raise TimeoutException(f"Element is not active")

    def _wait_element_enable(self, loc):
        end_time = time.time() + TIMEOUT
        while True:
            if self._check_element_enable(*loc):
                return True
            time.sleep(POLL_FREQUENCY)
            if time.time() > end_time:
                break
        raise TimeoutException(f"Element is not enabled")

    def _click_element(self, selector):
        self._wait_to_be_selected(*selector)
        element = self.driver.find_element(*selector)
        element.click()

    def _click_last_element(self, selector):
        self._wait_to_be_selected(*selector)
        last_element = self.driver.find_elements(*selector)[-1]
        last_element.click()
        
    def _update_page(self):
        self.driver.refresh()

    def click_element_by_mouse(self, selector):
        element = self.driver.find_element(*selector)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def _verify_element_with_text(self, text):
        locator = (By.XPATH, f"//*[text()='{text}']")
        asserts.assert_true(self._is_element_visible(*locator), f"Element with '{text}' is not visible")

    def _verify_no_element_with_text(self, text):
        locator = (By.XPATH, f"//*[text()='{text}']")
        asserts.assert_false(self._is_element_visible(*locator), f"Element with '{text}' is visible")

    def _verify_elements_with_text(self, texts):
        for text in texts:
            self._verify_element_with_text(text)

    def _verify_element_contains_text(self, text):
        locator = (By.XPATH, f"//*[contains(text(), {text})]")
        asserts.assert_true(self._is_element_visible(*locator), f"Element containing '{text}' is not visible")
