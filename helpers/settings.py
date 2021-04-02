
"""
Module contains settings.
"""

import helpers.generators
from os import environ
from dotenv import load_dotenv

load_dotenv()

BASE_HOST_NOTARY = environ.get('NOTARY_WEB_HOST_EXTERNAL')
# BASE_HOST_SERVICE = 'https://stage.midhub.org/service/reg'
BASE_USER_PIN = "0000"
BASE_HOST_CORE_RPC = environ.get('CORE_RPC_HOST_EXTERNAL').rstrip('/')

SELENIUM_HUB_URL = environ.get('SELENIUM_HUB_URL', 'http://selenium-hub:4444/wd/hub')
CREATE_ASSIGNED_APP = '{}/api/issue/create?pin={}'.format(BASE_HOST_CORE_RPC, helpers.generators.get_random_digit(4))

def create_form(get_pin):
    CREATE_FORMED_APP = '{}/api/issue/form?pin={}'.format(BASE_HOST_CORE_RPC, get_pin)
    return CREATE_FORMED_APP

def issue_documents(get_pin):
    ISSUE_DOC = '{}/api/issue?pinPrefix={}'.format(BASE_HOST_CORE_RPC, get_pin)
    return ISSUE_DOC

def create_company(get_pin, company_name ):
    CREATE_COMPANY = "{}/api/create-company?founderPin={}&name={}".format(BASE_HOST_CORE_RPC, get_pin, company_name)
    return CREATE_COMPANY

GRANT_PERMISSON = BASE_HOST_CORE_RPC+"/api/permissions/grant?pin={}"
