from django.contrib import admin

from sweetshop.contact.models import ContactForm


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    pass