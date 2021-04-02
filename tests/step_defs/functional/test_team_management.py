from pytest_bdd import scenarios, given, when, then, parsers
import requests
import pytest
from pages.AdminMainPagePO import AdminMainPagePO
from pages.TeamManagementPO import TeamManagementPO
from pages.TeamManagementFormPO import TeamManagementFormPO
from blocks.SideMenuBO import SideMenuBO


scenarios("./team_management.feature", strict_gherkin=False)

@when("I click Team Management")
def click_team_management(browser):
    SideMenuBO(browser).go_to_team_management()


@then("I verify Team Management page")
def verify_team_management(browser):
    TeamManagementPO(browser).verify_connect_partners_page_base()


@when("I expand Invite Employee block")
def expand_invite_employee(browser):
    TeamManagementPO(browser).waiter().click_add_new_employee()


@when("I input address of employee")
def input_employee_address(browser, session_vars):
    TeamManagementPO(browser).fill_address(session_vars['address'])


@when("I click the checkbox in Invite Employee block")
def click_checkbox(browser):
    TeamManagementPO(browser).waiter().click_checkbox()


@when("I click invite button in Invite Employee block")
def click_invite_btn(browser):
    TeamManagementPO(browser).waiter().click_invite_btn()


@when("I go to Pending authorization tab")
def open_pending_tab(browser):
    TeamManagementPO(browser).go_to_pending_auth_tab()


@then(parsers.parse('I should see permission with status "{status}"'))
def check_permission_on_pending(browser, status, session_vars):
    TeamManagementPO(browser).verify_permission(session_vars['address'], status)


@then("I should see Open button in permission")
def check_open_button(browser):
    TeamManagementPO(browser).verify_permission_grant()

@when("I click Open permission button")
def click_open_permission(browser):
    TeamManagementPO(browser).open_permission()


@when("I verify check document page")
def verify_team_management_form(browser):
    TeamManagementFormPO(browser).verify_page()


@when("I click Manager button")
def click_manager_button(browser):
    TeamManagementFormPO(browser).click_manager_btn()


@when("I click Employee button")
def click_employee_button(browser):
    TeamManagementFormPO(browser).click_employee_btn()


@then("I am on Authorized employees tab")
def wait_active_authorized_employees(browser):
    TeamManagementPO(browser).waiter().wait_active_authorized_employees_tab()
