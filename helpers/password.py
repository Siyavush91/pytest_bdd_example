"""
Contain function for encrypting user's password.
"""
import hashlib
import logging
from models.password import Password


def encrypt_user_password(password: Password, salt: Password, encoding='utf-8') -> Password:
    """
    Provide user's password encryption.

    :param password: user's password.
    :param salt: salt data from db table oc_customer.
    :param encoding: utf-8 encoding.
    :return: Password object with hash data.
    """
    logging.info(f"Convert password: {password} and salt: {salt} into hashed password.")
    step1 = hashlib.sha1(password.password.encode(encoding))
    step2 = hashlib.sha1(salt.salt.encode(encoding) + step1.hexdigest().encode(encoding))
    step3 = hashlib.sha1(salt.salt.encode(encoding) + step2.hexdigest().encode(encoding))
    return Password(password=step3.hexdigest())
