"""
Generator of random emails, digits, names, passwords.
"""
import random
import string

import allure

DOMAINS = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]
LETTERS = string.ascii_lowercase
DIGITS = string.digits
PASSWORDS = string.hexdigits


def get_random_domain(_domains):
    """Return random domain from _domains list."""
    return random.choice(_domains)


def get_random_digit(length):
    """Return random numeric value in string of presetted length."""
    return ''.join(random.choice(DIGITS) for i in range(length))


def get_random_name(length):
    """Return random string of presetted length."""
    return ''.join(random.choice(LETTERS) for i in range(length))


def get_random_password(length):
    """Return random alphanumeric value in string of presetted length."""
    return ''.join(random.choice(PASSWORDS) for i in range(length))


def generate_random_email(length):
    """Return random email address in string with presetted length of local-part."""
    return [get_random_name(length) + '@' + get_random_domain(DOMAINS)]
