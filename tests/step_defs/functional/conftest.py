from pytest_bdd import scenarios, given, when, then, parsers
from pages.ApplicationPO import ApplicationPO
from pages.AdminMainPO import AdminMainPO
from pages.DomainsMainPO import DomainsMainPO
from pages.DomainManagementPO import DomainManagementPO
from blocks.SideMenuBO import SideMenuBO
from helpers.settings import create_form, GRANT_PERMISSON
import helpers.generators
import allure
import requests
import pytest
import time
from helpers.settings import issue_documents
from pages.AdminMainPagePO import AdminMainPagePO
from pages.ApplicationFormPO import ApplicationFormPO
from selenium.common.exceptions import TimeoutException

#fixtures for work pages
@given("User send document in the pool and I get it")
def create_formed_app(session_vars):
    user_pin = helpers.generators.get_random_digit(5)
    response = requests.get(create_form(user_pin))
    json_response = response.json()
    session_vars['doc_in_pool'] = json_response['applicationId']


# shared steps work pages
@when("I get to the Application page")
def wait_btn(browser):
    ApplicationPO(browser).waiter()


#fixtures for admin pages
@given("MidHub verifies user ownership documents via bot")
def issue_document(session_vars):
    user_pin = helpers.generators.get_random_digit(5)
    response = requests.get(issue_documents(user_pin))
    json_response = response.json()
    session_vars['address'] = json_response[0]['masterAddress']
    session_vars['user_pin'] = user_pin

#shared steps admin pages
@when("I click work button")
def open_work(browser):
    SideMenuBO(browser).go_to_work()


@when("I click admin button")
def open_admin(browser):
    SideMenuBO(browser).go_to_admin()


@then("I am on Admin page")
def wait_admin_page(browser):
    AdminMainPagePO(browser).waiter()


@then("I verify Admin page")
def verify_admin_page(browser):
    AdminMainPagePO(browser).verify_admin_page()


@when("User accepts permission via bot")
def get_permission(browser, session_vars):
    end_time = time.time() + 15
    while True:
        response = requests.get(GRANT_PERMISSON.format(session_vars['user_pin'])).json()
        if "privateKey" in response:
            return True
        time.sleep(0.5)
        if time.time() > end_time:
            break
    raise TimeoutException(f"Call /mh-bot/api/permissions/grant was not successful")


@when(parsers.parse('I choose domain "{domain_name}" in filters'))
def choose_domain_in_filters(browser, domain_name):
    page = ApplicationPO(browser).waiter()
    page.tap_domain_filters_btn()
    page.open_domain_selector()
    page.choose_domain(domain_name)


@when("I click request button")
def step_impl(browser):
    ApplicationPO(browser).click_request_button()


@when("I click request button until pool is empty")
def click_request_empty_pool(browser, session_vars):
    end_time = time.time() + 15
    while True:
        if ApplicationPO(browser).toast_visible():
            session_vars['doc_in_pool'] = ApplicationPO(browser).waiter().get_last_application_id()
            return True
        time.sleep(1.5)
        ApplicationPO(browser).click_request_button()
        if time.time() > end_time:
            break
    raise TimeoutException(f"Infinite requests of applications")


@when("I wait until request button is active")
def wait_active_request_btn(browser):
    ApplicationPO(browser).wait_active_request_button()


@then("I should see user empty document")
def verify_empty_doc(browser, session_vars):
    ApplicationPO(browser).waiter().verify_empty_application(session_vars['doc_in_pool'])


@then("I verify formed application")
def check_formed_app(browser, session_vars):
    ApplicationPO(browser).verify_application(session_vars['doc_in_pool'])


@when("I click on application")
def click_app(browser, session_vars):
    ApplicationPO(browser).goto_app_form(session_vars['doc_in_pool'])


@then("I should see document page")
def check_btn_texts(browser):
    ApplicationFormPO(browser).verify_document()


@when("I click checkbox")
def click_checkbox(browser):
    ApplicationFormPO(browser).click_agree_checkbox()


@when("Click Accept button")
def step_impl(browser):
    ApplicationFormPO(browser).click_accept_button()


@when("I'm land on Application page")
def step_impl(browser):
    ApplicationPO(browser).waiter()


@then("I should see application disappeared after several page refreshes")
def step_impl(browser, session_vars):
    ApplicationPO(browser).waiter().verify_lack_of_application(session_vars['doc_in_pool'])


@when("I click Domains")
def open_domain(browser):
    SideMenuBO(browser).go_to_domains()


@then("I verify Domains page")
def verify_domains(browser):
    DomainsMainPO(browser).verify_page()


@when("I click Midhub Global")
def click_midhub_global(browser):
    DomainsMainPO(browser).open_mh_global()


@then("I verify MH Global Management page")
def verify_mh_global_management(browser):
    DomainManagementPO(browser).verify_domain_managment_page()
