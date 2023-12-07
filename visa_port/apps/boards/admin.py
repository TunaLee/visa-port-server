from django.contrib import admin

from com_duck.apps.boards.models.index import Board
from com_duck.bases.admin import Admin


@admin.register(Board)
class BoardAdmin(Admin):
    list_display = ('category', 'name')
    search_fields = ('',)
    readonly_fields = ('',)

    fieldsets = (
        ("정보", {"fields": ('category', 'name')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('category', 'name')}),
    )
