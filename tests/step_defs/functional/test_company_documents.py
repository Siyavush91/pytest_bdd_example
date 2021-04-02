from pytest_bdd import scenarios, given, when, then, parsers
from pages.AdminMainPagePO import AdminMainPagePO
from pages.CompanyDocumentsMainPO import CompanyDocumentsMainPO
from pages.InProcessPO import InProcessPO
from pages.ChooseDocumentPO import ChooseDocumentPO
from pages.DocumentTemplatePO import DocumentTemplatePO
from pages.DocumentPO import DocumentPO
from pages.DocumentPreviewPO import DocumentPreviewPO
from pages.DomainsMainPO import DomainsMainPO
from pages.VerificationTypeSelectionPO import VerificationTypeSelectionPO
from blocks.SideMenuBO import SideMenuBO
from helpers import constants

scenarios("./company_documents.feature", strict_gherkin=False)

@when("I click Company Documents")
def click_ompany_docs(browser):
    SideMenuBO(browser).go_to_company_documents()


@then("I verify Company Documents")
def verify_company_docs(browser):
    CompanyDocumentsMainPO(browser).verify_page()


@when("I wait when loader disappeared on Company Documents screen")
def loader_disappeared(browser):
    CompanyDocumentsMainPO(browser).wait_loader_not_displayed()


@when("I click Add document")
def click_add_doc(browser):
    CompanyDocumentsMainPO(browser).waiter().click_add_doc()


@when(parsers.parse('I choose domain "{domain}" on Choose Document screen'))
def choose_domain(browser, domain):
    ChooseDocumentPO(browser).waiter().choose_domain(domain)


@then(parsers.parse('I verify "{documents}" in list on Add Doc screen'))
def verify_elements_on_add_doc(browser, documents):
    page = ChooseDocumentPO(browser).waiter()
    elements = documents.split(', ')
    for element in elements:
        page.verify_document(element)


@when(parsers.parse('I click on "{doc}" on Add Doc screen'))
def click_doc(browser, doc):
    page = ChooseDocumentPO(browser).waiter()
    page.choose_document(doc)


@then(parsers.parse('I verify "{name}" template form'))
def verify_template(browser, name):
    if name == constants.RF_PASSPORT:
        DocumentTemplatePO(browser).verify_rf_passport_template()
    else:
        raise("Not supported template")


@when(parsers.parse('I fill text field "{field}" with value "{value}"'))
def fill_text_value(browser, field, value):
    DocumentTemplatePO(browser).fill_text_field(field, value)


@when(parsers.parse('I select "{value}" for field "{field}"'))
def fill_select_value(browser, field, value):
    DocumentTemplatePO(browser).select_value(field, value)


@when("I add 2 photos on template form")
def add_photos(browser):
    DocumentTemplatePO(browser).add_photo()
    DocumentTemplatePO(browser).add_photo()


@when("I click Next button on template form")
def click_next_btn(browser):
    DocumentTemplatePO(browser).click_next_btn()


@then(parsers.parse('I verify "{value}" on Company Documents page'))
def verify_company_doc(browser, value):
    CompanyDocumentsMainPO(browser).waiter().verify_doc(value)


@then(parsers.parse('I verify no "{value}" on Company Documents page'))
def verify_no_company_doc(browser, value):
    CompanyDocumentsMainPO(browser).waiter().verify_no_doc(value)


@when(parsers.parse('I click on "{value}" on Company Documents page'))
def click_company_doc(browser, value):
    CompanyDocumentsMainPO(browser).waiter().click_on_doc(value)


@then(parsers.parse('I verify Document page "{document_type}" for "{test_data}"'))
def verify_doc(browser, document_type, test_data):
    if test_data == 'Test User1':
        data_set = constants.TEST_USER1_DATA
    DocumentPO(browser).verify_page(document_type, data_set)


@when('I click "Send to validation" button')
def click_send_to_validation(browser):
    DocumentPO(browser).click_send_to_validation()


@then("I verify Verification Type Selection page")
def verify_verification_type(browser):
    VerificationTypeSelectionPO(browser).verify_page()


@when('I choose green global verification')
def click_green_global(browser):
    VerificationTypeSelectionPO(browser).click_green_global()


@then(parsers.parse('I verify Document Preview page "{document_type}" for "{test_data}" with header'))
def verify_doc_preview_with_header(browser, document_type, test_data):
    if test_data == 'Test User1':
        data_set = constants.TEST_USER1_DATA
    check_header = True
    DocumentPreviewPO(browser).verify_page(document_type, data_set, check_header)


@then(parsers.parse('I verify Document Preview page "{document_type}" for "{test_data}"'))
def verify_doc_preview(browser, document_type, test_data):
    if test_data == 'Test User1':
        data_set = constants.TEST_USER1_DATA
    check_header = False
    DocumentPreviewPO(browser).verify_page(document_type, data_set, check_header)


@then('I verify encryption buttons on Document Preview page')
def verify_encryption_buttons(browser):
    DocumentPreviewPO(browser).verify_encrypt_buttons()


@then('I verify no encryption buttons on Document Preview page')
def verify_no_encryption_buttons(browser):
    DocumentPreviewPO(browser).verify_no_encrypt_buttons()


@then('I verify sign and report buttons on Document Preview page')
def verify_sign_and_report_buttons(browser):
    DocumentPreviewPO(browser).verify_sign_and_report_buttons()


@then('I verify send to validator button on Document Preview page')
def verify_send_to_validator_button(browser):
    DocumentPreviewPO(browser).verify_send_to_validator_button()


@then('I verify green global verification on Document Preview Page')
def verify_verification_on_preview(browser):
    DocumentPreviewPO(browser).verify_global_green_verification()


@when('I click "Send to validator" button')
def click_send_to_validator(browser):
    DocumentPreviewPO(browser).click_send_to_validator()


@when('I click "Encrypt to validator" button')
def click_encrypt_to_validator(browser):
    DocumentPreviewPO(browser).click_encrypt_to_validator()


@when('I click "Sign" button')
def click_sign(browser):
    DocumentPreviewPO(browser).click_sign()


@when('I go to In process tab')
def open_in_progress(browser):
    CompanyDocumentsMainPO(browser).waiter().open_in_progress_tab()


@then("I verify In process page")
def verify_in_process(browser):
    InProcessPO(browser).verify_page()


@then(parsers.parse('I verify "{value}" with status "{status}" for "{verification_type}" verification on In process page'))
def verify_doc_in_process(browser, value, status, verification_type):
    if status == "Waiting for signing":
        status_text = constants.DOC_STATUS_WAITING
    elif status == "Assigned to notary":
        status_text = constants.DOC_STATUS_ASSIGNED
    else:
        raise('Unsupported status')

    if "Green" in verification_type:
        verification_colour = "GRN"
    else:
        raise('Unsupported verification colour')

    if "Global" in verification_type:
        verification_type = constants.GLOBAL_HEADER
    else:
        raise('Unsupported verification type')

    InProcessPO(browser).waiter().verify_doc(value, status_text, verification_colour, verification_type)


@when(parsers.parse('I click on "{value}" on In process page'))
def click_in_process_doc(browser, value):
    InProcessPO(browser).waiter().click_on_doc(value)