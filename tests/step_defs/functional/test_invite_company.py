from pytest_bdd import scenarios, given, when, then, parsers
import requests
import pytest
from pages.ConnectPartnersPO import ConnectPartnersPO
from pages.ConnectPartnersFormPO import ConnectPartnersFormPO
from pages.AdminMainPagePO import AdminMainPagePO
from pages.AdminLoginPO import AdminLoginPO
from pages.InvitePolicyPO import InvitePolicyPO
from pages.InviteCompanySetupPO import InviteCompanySetupPO
from pages.NicknameFormPO import NicknameFormPO
from blocks.SideMenuBO import SideMenuBO
from blocks.HeaderBO import HeaderBO
from helpers.settings import GRANT_PERMISSON
from helpers import constants


scenarios("./invite_company.feature", strict_gherkin=False)

@then(parsers.parse('I verify approval page for "{company_name}"'))
def check_page(browser, company_name):
    ConnectPartnersFormPO(browser).verify_form(company_name)

@when("I click Open button")
def open_permisson(browser):
    ConnectPartnersPO(browser).open_permission()

@when("I click Connect partners")
def open_connect_partners(browser):
    SideMenuBO(browser).go_to_connect_partners()


@then("I verify Connect partners page")
def check_connect_partners(browser):
    ConnectPartnersPO(browser).verify_connect_partners_page_base()


@then("I verify expanded Add New Partner block")
def verify_expanded_add_new_partner(browser):
    ConnectPartnersPO(browser).verify_add_partner_block_expanded()


@when("I click Add new partner link on Connect partners page")
def click_add_new_partner(browser):
    ConnectPartnersPO(browser).waiter().click_add_new_partner()

@when(parsers.parse('I fill company name "{company_name}" field'))
def fill_company_name(browser, company_name):
    ConnectPartnersPO(browser).fill_company_name(company_name)

@when("I input address field")
def input_address(browser, session_vars):
    ConnectPartnersPO(browser).fill_address(session_vars['address'])

@when("I click the checkbox")
def click_checkbox(browser):
    ConnectPartnersPO(browser).click_checkbox()

@when("Click invite button")
def invite_user(browser):
    ConnectPartnersPO(browser).click_invite_btn()


@then(parsers.parse('I verify "{company_name}" with status "{status}" in Requested partners tab'))
def requested_partners_status(browser, company_name, status, session_vars):
    if status == "Waiting for confirmation":
        status_text = constants.WAITING_STATUS
    elif status == "Accepted":
        status_text = constants.ACCEPTED_STATUS
    else:
        raise NotImplementedError(u'Not supported status')
    ConnectPartnersPO(browser).waiter().verify_invited_company(company_name, session_vars['address'], status_text)


@then("I am on Connect partners page")
def wait_connect_partners(browser):
    ConnectPartnersPO(browser).waiter()


@when("I click invite button")
def step_impl(browser):
    ConnectPartnersFormPO(browser).waiter().click_accept_btn()


@when("I click cancel button")
def step_impl(browser):
    ConnectPartnersFormPO(browser).waiter().click_decline_btn()

@then("I should see permisson disappeared")
def step_impl(browser, session_vars):
    ConnectPartnersPO(browser).waiter().check_permisson_dissapeared(session_vars['address'])


@then("I verify Invite Company Setup page")
def step_impl(browser):
    InviteCompanySetupPO(browser).verify_page()


@when("I fill an address field")
def step_impl(browser, session_vars):
    InviteCompanySetupPO(browser).input_executive_address(session_vars['address'])

@when("I invite executive")
def step_impl(browser):
    InviteCompanySetupPO(browser).invite_members()


@when("Executive accepts the invitation via bot")
def grant_permission_by_bot(session_vars):
    response = requests.get(GRANT_PERMISSON.format(session_vars['user_pin']))


@then("I should see executive document")
def step_impl(browser):
    InviteCompanySetupPO(browser).verify_invited_members()


# @given('Text in invite button change on "Завершить настройку"')
# def step_impl():
#     raise NotImplementedError(u'STEP: And  Text in invite button change on "Завершить настройку"')


@when('I click finish settings')
def step_impl(browser):
    InviteCompanySetupPO(browser).finish_setup()


@when("I click cancel company button")
def step_impl(browser):
    InviteCompanySetupPO(browser).cancel_create_company()
