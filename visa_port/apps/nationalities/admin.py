from django.contrib import admin

from visa_port.apps.nationalities.models import Nationality
from visa_port.bases.admin import Admin


@admin.register(Nationality)
class NationalityView(Admin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    # readonly_fields = ('',)

    fieldsets = (
        ("정보", {"fields": ('code', 'name')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('code', 'name')}),
    )
