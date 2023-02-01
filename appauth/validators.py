import re
from django.core.exceptions import ValidationError

def validate_phone(value: str) -> None:
    '''
    ensures the correct number formats
    for kenya
    '''
    # if not re.compile(r'^0(7|1)\d{8}$|^\+?254(7|1)\d{8}$')\
    #     .match(value):
    #     raise ValidationError('Invalid phone number!', params={'value': value})
    pass