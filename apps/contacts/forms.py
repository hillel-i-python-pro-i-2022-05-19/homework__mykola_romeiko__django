from django import forms

from apps.contacts.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'birthday',
            'contact_details_by_foreign_key',
            'tag_many_to_many',
        )
