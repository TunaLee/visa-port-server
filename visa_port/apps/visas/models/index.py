# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

from visa_port.apps.visas.models.mixins.renewal import VisaRenewalMixin
from visa_port.apps.visas.models.mixins.view import VisaViewMixin
# Local
from visa_port.bases.models import Model


class VisaCode(Model):
    name = models.TextField(_('비자 코드명'))
    description = models.TextField(_('비자 코드 설명'))
    class Meta:
        verbose_name = verbose_name_plural = _('비자 코드')
        db_table = 'visa_code'
        ordering = ['name']

class Visa(Model,
           VisaViewMixin,
           VisaRenewalMixin
           ):
    code = models.ForeignKey(VisaCode, related_name='visas', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey('users.User', related_name='visas', on_delete=models.SET_NULL, null=True, blank=True)
    nationality = models.ForeignKey('nationalities.Nationality', related_name='visas', on_delete=models.SET_NULL, null=True, blank=True)

    passport_no = models.TextField(primary_key=True, verbose_name=_('여권 번호'))
    expiration_date = models.DateField(_('비자 만료일'))

    class Meta:
        verbose_name = verbose_name_plural = _('비자')
        db_table = 'visa'
        ordering = ['-created']
