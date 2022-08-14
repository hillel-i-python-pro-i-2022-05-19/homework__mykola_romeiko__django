from django.contrib import admin

from apps.contacts.models import Contact, ContactDetail, Tag

admin.site.register(Contact)
admin.site.register(ContactDetail)
admin.site.register(Tag)
