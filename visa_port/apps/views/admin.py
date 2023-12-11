from django.contrib import admin

from visa_port.apps.views.models import ExpirationView
from visa_port.bases.admin import Admin


@admin.register(ExpirationView)
class ExpirationViewsView(Admin):
    list_display = ('passport_no', 'expiration_date', 'birth_date', 'nationality', 'visa_code')
    search_fields = ('passport_no', 'expiration_date', 'birth_date', 'nationality', 'visa_code')
    readonly_fields = ('passport_no', 'expiration_date', 'birth_date', 'nationality', 'visa_code')

    fieldsets = (
        ("정보", {"fields": ('passport_no', 'expiration_date', 'birth_date', 'nationality', 'visa_code')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('passport_no', 'expiration_date', 'birth_date', 'nationality', 'visa_code')}),
    )
