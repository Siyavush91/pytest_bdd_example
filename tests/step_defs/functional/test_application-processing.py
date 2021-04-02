from pytest_bdd import scenarios, given, when, then
from pages.ApplicationPO import ApplicationPO
from pages.ApplicationFormPO import ApplicationFormPO

scenarios("./application_processing.feature", strict_gherkin=False)


@when("Click Reject button")
def step_impl(browser):
    ApplicationFormPO(browser).click_decline_button()


@then("I see popup with input field for message")
def step_impl(browser):
    ApplicationFormPO(browser).verify_popup()


@when("I input message and click Send button")
def step_impl(browser):
    ApplicationFormPO(browser).fill_decline_comment_popup("комментарий")


@when("I click suspend button")
def step_impl(browser):
    ApplicationFormPO(browser).click_suspend_button()


@when("I go to In proccess page")
def step_impl(browser):
    ApplicationPO(browser).goto_app_on_hold()
