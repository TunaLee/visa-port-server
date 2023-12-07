from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BoardsConfig(AppConfig):
    name = "com_duck.apps.boards"
    verbose_name = _('게시판 관리')
