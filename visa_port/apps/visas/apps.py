from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VisaConfig(AppConfig):
    name = "visa_port.apps.visas"
    verbose_name = _('비자 관리')
