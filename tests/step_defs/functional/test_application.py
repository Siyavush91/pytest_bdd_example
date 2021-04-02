from pytest_bdd import scenarios, given, when, then, parsers
from helpers.settings import CREATE_ASSIGNED_APP
import requests
from pages.ApplicationPO import ApplicationPO
from pages.ApplicationFormPO import ApplicationFormPO

scenarios('./application-request.feature', strict_gherkin=False)


@when("User put empty document in pool")
def create_empty_app(session_vars):
    response = requests.get(CREATE_ASSIGNED_APP)
    json_response = response.json()
    session_vars['doc_in_pool'] = json_response['applicationId']


@then(parsers.parse('I verify "{domain_name}" is chosen in filters'))
def verify_domain_in_filters(browser, domain_name):
    ApplicationPO(browser).waiter().verify_chosen_domain(domain_name)


@then("I should see No Applications toast")
def check_toast(browser):
    page = ApplicationPO(browser).waiter()
    page.verify_toast()


@when("I verify Application page")
def verify_page(browser):
    ApplicationPO(browser).waiter().verify_application_request_container()
