from django.contrib import admin

from visa_port.apps.nationalities.models import Nationality
from visa_port.bases.admin import Admin


@admin.register(Nationality)
class NationalityView(Admin):
    list_display = ('',)
    search_fields = ('',)
    readonly_fields = ('',)

    fieldsets = (
        ("정보", {"fields": ('',)}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('',)}),
    )
