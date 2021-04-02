from pytest_bdd import scenarios, given, when, then, parsers
from pages.BasePO import BasePO
from pages.DomainsMainPO import DomainsMainPO
from pages.DomainManagementPO import DomainManagementPO
from pages.AdminMainPagePO import AdminMainPagePO
from pages.CreateSubdomainPO import CreateSubdomainPO
from blocks.SideMenuBO import SideMenuBO
from helpers import constants, generators
import time

scenarios("./domains.feature", strict_gherkin=False)


@then("I verify created domain on Domain Management page")
def verify_created_domain(browser, session_vars):
    DomainManagementPO(browser).waiter().verify_domain(session_vars['domain_name'])


@when("I update Domain Management page")
def update_domain_management(browser):
    DomainManagementPO(browser).waiter()
    time.sleep(3)
    BasePO(browser)._update_page()


@when("I open Subdomain menu")
def open_subdomain_menu(browser):
    DomainManagementPO(browser).open_subdomain_menu()


@when(parsers.parse('I choose "{option}" option in Subdomain menu'))
def choose_option(browser, option):
    if option == 'Create subdomain':
        DomainManagementPO(browser).choose_option(option)
    else:
        raise('Unsupported option')


@then("I verify Subdomain menu options")
def verify_subdomain_menu(browser):
    DomainManagementPO(browser).verify_subdomain_menu()


@then("I verify Create Subdomain page")
def verify_create_subdomain(browser):
    CreateSubdomainPO(browser).verify_page()


@when("I fill test domain name")
def input_domain_name(browser, session_vars):
    session_vars['domain_name'] = "Test" + generators.get_random_digit(5)
    CreateSubdomainPO(browser).waiter().fill_domain_name(session_vars['domain_name'])


@when("I fill country code")
def input_country_code(browser):
    country_code = "Code" + generators.get_random_digit(4)
    CreateSubdomainPO(browser).waiter().fill_country_code(country_code)


@when("I accept rules on Create Subdomain page")
def accept_rules(browser):
    CreateSubdomainPO(browser).waiter().accept_rules()


@when("I tap create button on Create Subdomain page")
def tap_create_domain(browser):
    CreateSubdomainPO(browser).waiter().tap_create_btn()
