"""
This module contains shared fixtures for web UI tests.
"""

import json

import allure
import pytest
import subprocess
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from helpers.project_logger.logs.project_logger import logger
from pytest_bdd import scenario, scenarios, given, when, then, parsers
from selenium.webdriver import Chrome, Firefox
from helpers.settings import BASE_HOST_NOTARY, BASE_USER_PIN, SELENIUM_HUB_URL
from pages.AdminLoginPO import AdminLoginPO
from pages.WelcomePO import WelcomePO
from pages.AdminMainPO import AdminMainPO
from blocks.SideMenuBO import SideMenuBO
from blocks.HeaderBO import HeaderBO
from pages.InvitePolicyPO import InvitePolicyPO
from pages.NicknameFormPO import NicknameFormPO
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# @todo implement video_recording again with docker
# from helpers.video_recording import screenshot_capturing

CONFIG_PATH = 'tests/step_defs/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']

# Hooks

# Browser Fixtures
@pytest.fixture(scope="session")
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture(scope="session")
def session_vars():
    session_vars = {
        "address" : '',
        "user_pin" : '',
        "doc_in_pool": '',
        "domain_name": '',
        "template_name": '',
        "template_desc": '',
        "template_code": '',
        "template_category": '',
        "requirement_name": '',
        "requirement_desc": ''
    }
    return session_vars

@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the browser choice from the config data
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def browser(request, config_browser, config_wait_time):
    # Initialize WebDriver
    if config_browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif config_browser == 'chrome-local':
        options = webdriver.ChromeOptions()
        options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://swarm_nginx,ws://eth-node-nginx:8546,http://eth-node-nginx:8545,http://client-backend-nginx,http://service-cdp:3010,http://client-api:10130,http://core-rpc:3700,http://notary_nginx")

        driver = webdriver.Remote(
            command_executor=SELENIUM_HUB_URL,
            desired_capabilities=options.to_capabilities())
    elif config_browser == 'firefox':
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)
    # open browser fullscreen
    driver.maximize_window()

    # @todo implement video_recording again with docker
    # video_recorder_process = subprocess.Popen(['python3', 'helpers/video_recording.py']).pid

    # Return the driver object at the end of setup
    yield driver
    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            driver.execute_script("document.body.bgColor = 'white';")
            # Attaching video to Allure
            # @todo implement video_recording again with docker
            # screenshot_capturing.terminate(video_recorder_process)
            # _attach_video_to_allure()

            # Attaching screenshot to Allure
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass # just ignore
    else:
        # @todo implement video_recording again with docker
        # screenshot_capturing.terminate(video_recorder_process)
        if logger.soft_assert_fail:
            logger.soft_assert_fail = False
            allure.attach("Traceback: \n" + logger.logs)
            # @todo implement video_recording again with docker
            # _attach_video_to_allure()
            raise Exception("There is a soft assertion failure")
        logger.logs = ""

    # For cleanup, quit the driver
    def fin():
        driver.close()
    request.addfinalizer(fin)

@pytest.fixture
def pytestbdd_strict_gherkin():
    return False    

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    # Attaching logs to Allure
    logger.logs_exception(str(exception))
    allure.attach.file(logger.logs_file_path(), attachment_type=allure.attachment_type.TEXT)
    logger.clean_log_file()

def _attach_video_to_allure():
    video_stream = open("movie.mp4", "rb").read()
    allure.attach(video_stream, name = 'Video attach', attachment_type=allure.attachment_type.MP4)

# Shared Steps
@given(u'Midhub auth page is displayed')
def mh_home(browser):
    browser.get(BASE_HOST_NOTARY)


@then(u"I verify Welcome screen")
def verify_welcome(browser):
    WelcomePO(browser).verify_page()


@when(u"I click welcome button")
def click_welcome(browser):
    WelcomePO(browser).waiter().click_welcome()


@then(u"I verify Admin Login screen")
def verify_admin_login(browser):
    AdminLoginPO(browser).verify_page()


@when(u"I enter a pin and login")
def login(browser):
    AdminLoginPO(browser).waiter().input_pin(BASE_USER_PIN) \
        .login_button_tappable() \
        .login()


@then("I should see admin main page")
def wait_admin_main_page(browser):
    AdminMainPO(browser).waiter()


@then("I verify admin main page")
def verify_admin(browser):
    AdminMainPO(browser).verify_screen()


@when("I wait when loader disappeared")
def loader_disappeared(browser):
    AdminLoginPO(browser).wait_loader_not_displayed()


@then(u'Midhub auth page is displayed')
def then_mh_home(browser):
    browser.get(BASE_HOST_NOTARY)


@when(u'I click go to processing')
def go_to_app_list(browser):
    AdminMainPO(browser).goto_application()


@when("I logging out")
def step_impl(browser):
    HeaderBO(browser).log_out()


@then("I should see Login page")
def step_impl(browser):
    AdminLoginPO(browser).verify_page()


@when("I logging in as another user")
def step_impl(browser, session_vars):
    AdminLoginPO(browser).waiter() \
        .input_pin(session_vars['user_pin']) \
        .login_button_tappable() \
        .login()


@then("I verify Privacy Policy page")
def step_impl(browser):
    InvitePolicyPO(browser).verify_page()


@when("I agree with privacy policy")
def step_impl(browser):
    InvitePolicyPO(browser).click_agree_checkbox() \
        .click_next_btn()


@then("I verify Nickname Form page")
def step_impl(browser):
    NicknameFormPO(browser).verify_page()


@then("I verify Nickname Extended Form page")
def step_impl(browser):
    NicknameFormPO(browser).verify_page()\
        .verify_additional_fields()


@when("I fill Nickname form")
def step_impl(browser):
    NicknameFormPO(browser).fill_nickname()\
        .finish_registration()


@when("I fill Nickname Extended form")
def step_impl(browser):
    NicknameFormPO(browser).fill_nickname()\
        .fill_address()\
        .fill_phone()\
        .finish_registration()


@then("I see admin main page")
def step_impl(browser):
    AdminLoginPO(browser).wait_loader_not_displayed()
