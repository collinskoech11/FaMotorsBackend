from django.contrib import admin
from .models import ContactForm
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('brand','email')

admin.site.register(ContactForm, ContactAdmin)