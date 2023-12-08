from django.contrib import admin

from visa_port.apps.app_templates.models.index import Template
from visa_port.bases.admin import Admin


@admin.register(Template)
class TemplateView(Admin):
    list_display = ('',)
    search_fields = ('',)
    readonly_fields = ('',)

    fieldsets = (
        ("정보", {"fields": ('',)}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('',)}),
    )
