from django.core.validators import RegexValidator, validate_email
from django.db import models


# Create your models here.
class ContactDetail(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(verbose_name='Phone number', help_text='It is a phone number.', validators=[phone_regex], max_length=17, unique=True)
    email = models.EmailField(verbose_name='Email', help_text='It is an email.', validators=[validate_email], max_length=254, unique=True)

    def __str__(self):
        return f'phone: {self.phone}, email: {self.email}'

    def __repr__(self):
        return f'<ContactDetail (phone: {self.phone}, email: {self.email})>'


class Tag(models.Model):
    name = models.CharField(verbose_name='Tag name', help_text='It is a tag.', max_length=16, unique=True)

    def __str__(self):
        return f'Tag - {self.name}'

    def __repr__(self):
        return f'<Tag (name: {self.name})>'


class Contact(models.Model):
    name = models.CharField(verbose_name='Contact name', help_text='It is a contact name.', max_length=200)
    birthday = models.DateField(verbose_name='Contact birthday', help_text='It is a contact birthday', blank=True, default=None)

    contact_details_by_foreign_key = models.ForeignKey(
        to=ContactDetail,
        related_name='contact_related_by_foreign_key',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    tag_many_to_many = models.ManyToManyField(
        to=Tag,
        related_name='contact_related_by_many_to_many',
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'name: {self.name}, birthday: {self.birthday}'

    def __repr__(self):
        return f'<Contact (name: {self.name}, birthday: {self.birthday})>'
