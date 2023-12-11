from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ViewsConfig(AppConfig):
    name = "visa_port.apps.views"
    verbose_name = _('조회 관리')
