# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from visa_port.bases.models import Model
from visa_port.apps.users.models import User


class ExpirationView(Model):
    passport_no = models.TextField(_('여권 번호'))
    expiration_date = models.DateField(_('만료일'))
    birth_date = models.DateField(_('생년월일'))
    nationality = models.ForeignKey('nationalities.Nationality', verbose_name=_('국적'), related_name='expiration_views', on_delete=models.SET_NULL, null=True)
    visa_code = models.ForeignKey('visas.VisaCode', verbose_name=_('비자 코드'), related_name='expiration_views', on_delete=models.SET_NULL, null=True)

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name = verbose_name_plural = _('만료일 조회')
        db_table = 'expiration_view'
        ordering = ['-created']
