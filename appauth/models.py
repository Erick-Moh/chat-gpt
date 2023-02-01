from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_phone

class CustomUser(AbstractUser):
    '''
    creating a customized user model
    to adding phone number and 
    email
    '''
    phone_number = models.CharField(max_length=50, validators=[validate_phone,], unique=True)
    email = models.EmailField(unique=True)
