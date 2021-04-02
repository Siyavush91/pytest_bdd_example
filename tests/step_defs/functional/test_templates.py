from pytest_bdd import scenarios, given, when, then, parsers
from pages.BasePO import BasePO
from pages.CreateTemplatePO import CreateTemplatePO
from pages.DomainManagementPO import DomainManagementPO
from pages.TemplatePO import TemplatePO
from helpers import constants, generators

scenarios('./templates.feature', strict_gherkin=False)

@when("I click Add template")
def click_add_template(browser):
    DomainManagementPO(browser).click_add_template()


@then("I verify Create template page")
def verify_create_template(browser):
    CreateTemplatePO(browser).verify_page() \
        .verify_default_values()


@when("I fill name field with test value on Create template page")
def fill_doc_name(browser, session_vars):
    session_vars['template_name'] = "Template name" + generators.get_random_digit(3)
    CreateTemplatePO(browser).waiter().fill_doc_name(session_vars['template_name'])


@when(parsers.parse('I select "{category}" category on Create template page'))
def choose_category(browser, category, session_vars):
    if category == 'Citizenship':
        session_vars['template_category'] = constants.CITIZENSHIP
    else:
        raise('Unsupported category')
    CreateTemplatePO(browser).waiter().choose_category(session_vars['template_category'])


@when(parsers.parse('I select {status} verification status on Create template page'))
def select_status(browser, status):
    page = CreateTemplatePO(browser).waiter()
    if status == 'with':
        page.select_status(True)
    elif status == 'without':
        page.select_status(False)
    else:
        raise("Unsupported status")


@when(parsers.parse('I select {doc_type} type on Create template page'))
def select_type(browser, doc_type):
    page = CreateTemplatePO(browser).waiter()
    if doc_type == 'unique':
        page.select_type(True)
    elif doc_type == 'not unique':
        page.select_type(False)
    else:
        raise("Unsupported type")


@when("I fill description field with test value on Create template page")
def fill_description(browser, session_vars):
    session_vars['template_desc'] = "Template description"
    CreateTemplatePO(browser).waiter().fill_description(session_vars['template_desc'])


@when("I fill code field with test value on Create template page")
def fill_code(browser, session_vars):
    session_vars['template_code'] = "Template code" + generators.get_random_digit(3)
    CreateTemplatePO(browser).waiter().fill_code(session_vars['template_code'])


@when("I click Add field button on Create template page")
def click_add_field(browser):
    CreateTemplatePO(browser).waiter().click_add_field()


@then("I verify add field form on Create template page")
def verify_add_field_form(browser):
    CreateTemplatePO(browser).waiter().verify_add_field_form()


@when("I close field form on Create template page")
def close_field_form(browser):
    CreateTemplatePO(browser).waiter().close_field_form()


@when(parsers.parse('I add "{name}" field on Create template page'))
def add_text_field(browser, name):
    page = CreateTemplatePO(browser).waiter()
    page.click_add_field()
    page.add_name_field(name)
    page.save_field_form()


@when(parsers.parse('I add "{name}" number field with exact number of characters "{number}" on Create template page'))
def add_number_field(browser, name, number):
    page = CreateTemplatePO(browser).waiter()
    page.click_add_field()
    page.add_name_field(name)
    page.choose_type_of_field('Number')
    # TODO: add number of characters check
    page.save_field_form()


@when(parsers.parse('I add "{name}" option field with "{options}" options on Create template page'))
def add_option_field(browser, name, options):
    page = CreateTemplatePO(browser).waiter()
    page.click_add_field()
    page.add_name_field(name)
    page.choose_type_of_field('Options')
    # TODO: add options check
    page.save_field_form()


@when(parsers.parse('I add "{name}" photo field on Create template page'))
def add_photo_field(browser, name):
    page = CreateTemplatePO(browser).waiter()
    page.click_add_field()
    page.add_name_field(name)
    page.choose_type_of_field('Photo')
    page.save_field_form()


@then(parsers.parse('I verify "{name}" field on Create template page'))
def verify_field(browser, name):
    CreateTemplatePO(browser).waiter().verify_field(name)


@when("I click Publish button on Create template page")
def click_publish_btn(browser):
    CreateTemplatePO(browser).waiter().click_publish_btn()


@then("I verify added template on MH Global Management page")
def verify_added_template(browser, session_vars):
    DomainManagementPO(browser).waiter().verify_added_template(session_vars['template_name'])


@when("I click on added template on MH Global Management page")
def click_on_template(browser, session_vars):
    DomainManagementPO(browser).waiter().click_on_template(session_vars['template_name'])


@then("I verify Template page")
def verify_template_page(browser, session_vars):
    TemplatePO(browser).waiter().verify_page(session_vars['template_name'])


@then("I verify test template name on Template page")
def verify_template_name(browser, session_vars):
    TemplatePO(browser).waiter().verify_template_name(session_vars['template_name'])


@then(parsers.parse('I verify "{category}" category on Template page'))
def verify_template_category(browser, category, session_vars):
    if category == 'Citizenship':
        category = constants.CITIZENSHIP
    else:
        raise('Unsupported category')
    TemplatePO(browser).waiter().verify_template_category(category)


@then(parsers.parse('I verify {status} verification status on Template page'))
def verify_template_status(browser, status, session_vars):
    page = TemplatePO(browser).waiter()
    if status == 'with':
        page.verify_template_status(True)
    elif status == 'without':
        page.verify_template_status(False)
    else:
        raise("Unsupported status")


@then(parsers.parse('I verify {template_type} type on Template page'))
def verify_template_type(browser, template_type, session_vars):
    page = TemplatePO(browser).waiter()
    if template_type == 'unique':
        page.verify_template_type(True)
    elif template_type == 'not unique':
        page.verify_template_type(False)
    else:
        raise("Unsupported type")


@then("I verify description field with test value on Template page")
def verify_template_desc(browser, session_vars):
    TemplatePO(browser).waiter().verify_template_desc(session_vars['template_desc'])


@then("I verify code field with test value on Template page")
def verify_template_code(browser, session_vars):
    TemplatePO(browser).waiter().verify_template_code(session_vars['template_code'])


@then(parsers.parse('I verify "{name}" field on Template page'))
def verify_text_field(browser, name):
    page = TemplatePO(browser).waiter()
    page.click_field(name)
    page.verify_text_field(name)
    page.click_field(name)


@then(parsers.parse('I verify "{name}" number field with exact number of characters "{number}" on Template page'))
def verify_number_field(browser, name, number):
    page = TemplatePO(browser).waiter()
    page.click_field(name)
    page.verify_number_field(name)
    page.click_field(name)
    # TODO: add number of characters check


@then(parsers.parse('I verify "{name}" option field with "{options}" options on Template page'))
def verify_option_field(browser, name, options):
    page = TemplatePO(browser).waiter()
    page.click_field(name)
    page.verify_option_field(name)
    page.click_field(name)
    # TODO: add options check


@then(parsers.parse('I verify "{name}" photo field on Template page'))
def verify_photo_field(browser, name):
    page = TemplatePO(browser).waiter()
    page.click_field(name)
    page.verify_photo_field(name)
    page.click_field(name)