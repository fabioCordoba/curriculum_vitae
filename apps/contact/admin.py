from django.contrib import admin

from apps.contact.models.contact import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
