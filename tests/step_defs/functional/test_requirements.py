from pytest_bdd import scenarios, given, when, then, parsers
from pages.DomainsMainPO import DomainsMainPO
from pages.RequirementsMainPO import RequirementsMainPO
from pages.CreateRequirementsPO import CreateRequirementsPO
from pages.RequirementPO import RequirementPO
from pages.BasePO import BasePO
from helpers import constants, generators
import time

scenarios("./requirements.feature", strict_gherkin=False)

@when("I click Requirements tab")
def go_to_verification(browser):
    DomainsMainPO(browser).go_to_requirements()


@then("I verify Requirements page")
def verify_requirements_page(browser):
    RequirementsMainPO(browser).verify_page()


@then(parsers.parse('I verify created requirement for "{domain}" domain with "{req_type}" type on Requirements page'))
def verify_created_requirement(browser, domain, req_type, session_vars):
    RequirementsMainPO(browser).waiter().verify_added_requirement(session_vars['requirement_name'], domain, req_type)


@when("I click create requirement")
def create_requirement_btn(browser):
    RequirementsMainPO(browser).waiter().go_to_create_requirement()


@when("I click on created requirement on Requirements page")
def click_requirement(browser, session_vars):
    RequirementsMainPO(browser).waiter().click_requirement(session_vars['requirement_name'])


@when("I update Requirements page")
def update_requirements_page(browser):
    RequirementsMainPO(browser).waiter()
    time.sleep(5)
    BasePO(browser)._update_page()


@then("I verify Create Requirements page")
def verify_create_requirement_page(browser):
    CreateRequirementsPO(browser).verify_page()


@then("I verify expanded docs section on Create Requirements page")
def verify_expanded_doc_section(browser):
    CreateRequirementsPO(browser).verify_expanded_doc_section()


@when("I fill test name on Create Requirements page")
def fill_requirement_name(browser, session_vars):
    session_vars['requirement_name'] = "Requirement name" + generators.get_random_digit(5)
    CreateRequirementsPO(browser).waiter().fill_requirement_name(session_vars['requirement_name'])


@when("I fill test description on Create Requirements page")
def fill_requirement_desc(browser, session_vars):
    session_vars['requirement_desc'] = "Requirement desc" + generators.get_random_digit(5)
    CreateRequirementsPO(browser).waiter().fill_requirement_desc(session_vars['requirement_desc'])


@when(parsers.parse('I choose domain "{domain}" on Create Requirements page'))
def choose_requirement_domain(browser, domain):
    CreateRequirementsPO(browser).waiter().choose_requirement_domain(domain)


@when(parsers.parse('I choose "{verification_type}" type of verification on Create Requirements page'))
def choose_requirement_type(browser, verification_type):
    CreateRequirementsPO(browser).waiter().choose_requirement_type(verification_type)


@when(parsers.parse('I enable checkbox "{requirement_type}" on Create Requirements page'))
def enable_type_checkbox(browser, requirement_type):
    CreateRequirementsPO(browser).waiter().enable_type_checkbox(requirement_type)


@when("I click Add document button on Create Requirements page")
def click_add_doc_btn(browser):
    CreateRequirementsPO(browser).waiter().click_add_doc_btn()


@when(parsers.parse('I open "{doc_section}" docs on Create Requirements page'))
def expand_docs_section(browser, doc_section):
    CreateRequirementsPO(browser).waiter().expand_docs_section(doc_section)


@when(parsers.parse('I enable checkbox "{doc_name}" doc on Create Requirements page'))
def enable_doc_checkbox(browser, doc_name):
    CreateRequirementsPO(browser).waiter().enable_doc_checkbox(doc_name)


@when("I click Choose button for doc on Create Requirements page")
def click_choose_doc_btn(browser):
    CreateRequirementsPO(browser).waiter().click_choose_doc_btn()


@then(parsers.parse('I verify added doc "{doc_name}" on Create Requirements page'))
def verify_added_doc(browser, doc_name):
    CreateRequirementsPO(browser).verify_added_doc(doc_name)


@when("I click Create requirement button on Create Requirements page")
def click_create_requirement(browser):
    CreateRequirementsPO(browser).waiter().click_create_requirement()


@then("I verify Requirement page")
def verify_requirement_page(browser):
    RequirementPO(browser).verify_page()


@then("I verify test name on Requirement page")
def verify_requirement_name(browser, session_vars):
    RequirementPO(browser).waiter().verify_requirement_name(session_vars['requirement_name'])


@then("I verify test description on Requirement page")
def verify_requirement_desc(browser, session_vars):
    RequirementPO(browser).waiter().verify_requirement_desc(session_vars['requirement_desc'])


@then(parsers.parse('I verify "{domain}" domain on Requirement page'))
def verify_domain(browser, domain):
    RequirementPO(browser).waiter().verify_domain(domain)


@then(parsers.parse('I verify "{verification_type}" type of verification on Requirement page'))
def verify_verification_type(browser, verification_type):
    RequirementPO(browser).waiter().verify_verification_type(verification_type)


@then(parsers.parse('I verify "{docs_type}" type for documents on Requirement page'))
def verify_docs_type(browser, docs_type):
    RequirementPO(browser).waiter().verify_docs_type(docs_type)


@then(parsers.parse('I verify "{doc}" doc on Requirement page'))
def verify_doc(browser, doc):
    RequirementPO(browser).waiter().verify_doc(doc)