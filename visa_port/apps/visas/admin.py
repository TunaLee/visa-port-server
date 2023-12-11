from django.contrib import admin

from visa_port.apps.visas.models import VisaCode
from visa_port.bases.admin import Admin


@admin.register(VisaCode)
class VisaCodeView(Admin):
    list_display = ('',)
    search_fields = ('',)
    readonly_fields = ('',)

    fieldsets = (
        ("정보", {"fields": ('',)}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('',)}),
    )
