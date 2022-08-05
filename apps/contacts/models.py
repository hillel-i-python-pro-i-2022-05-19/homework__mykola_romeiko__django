from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Contact(models.Model):
    contact_name = models.CharField(verbose_name='Contact name', help_text='It is a contact name.', max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_value = models.CharField(verbose_name='Phone number', help_text='It is a phone number.', validators=[phone_regex], max_length=17, unique=True)
