from django.contrib import admin

from visa_port.apps.visas.models import VisaCode
from visa_port.bases.admin import Admin


@admin.register(VisaCode)
class VisaCodeView(Admin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

    fieldsets = (
        ("정보", {"fields": ('name', 'description')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('name', 'description')}),
    )
