from helpers.project_logger.logs.project_logger import logger
import traceback
import sys

class Asserts():
    def assert_equal(self, value1, value2):
        assert value1 == value2, f"{value1} is not equal {value2}"

    def assert_not_equal(self, value1, value2):
        assert not value1 == value2, f"{value1} is equal {value2}"

    def assert_true(self, value, error_message):
        assert value, error_message

    def assert_false(self, value, error_message):
        assert not value, error_message

    def assert_in(self, value, dict):
        assert value in dict.values(), f"{value} is not in {dict.values()}"

    def assert_is_not_none(self, value):
        assert value is not None

    def soft_assert_equal(self, value1, value2):
        try:
            self.assert_equal(value1, value2)
        except AssertionError as e:
            self.handle_exception(e)

    def soft_assert_in(self, value1, value2):
        try:
            self.assert_in(value1, value2)
        except AssertionError as e:
            self.handle_exception(e)

    def soft_assert_false(self, value, error_message):
        try:
            self.assert_false(value, error_message)
        except AssertionError as e:
            self.handle_exception(e)

    def soft_assert_true(self, value, error_message):
        try:
            self.assert_true(value, error_message)
        except AssertionError as e:
            self.handle_exception(e)

    def soft_assert_is_not_none(self, value):
        try:
            assert value is not None
        except AssertionError as e:
            self.handle_exception(e)

    def handle_exception(self, e):
        logger.soft_assert_fail = True
        stack_trace = ''.join(map(str, traceback.format_list(traceback.extract_stack(limit=15))))
        logger.logs_warning(stack_trace + '\n' + str(e))

asserts = Asserts()