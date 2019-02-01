# coding: utf-8
import re

def validate(password):
    if len(password) < 6:
        return False
    if re.compile(r'[0-9]').search(password) is None:
        return False
    if re.compile(r'[a-zA-Z]').search(password) is None:
        return False
    if re.compile(r'(.)\1\1').search(password) is not None:
        return False
    return True

input_password = input()

if validate(input_password):
    print("Valid")
else:
    print("Invalid")
    
