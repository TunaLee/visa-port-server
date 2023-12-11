# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from visa_port.bases.models import Model


class Nationality(Model):
    code = models.SmallIntegerField(unique=True, verbose_name=_('국적 코드'))
    name = models.TextField(unique=True, verbose_name=_('국적명'))
    class Meta:
        verbose_name = verbose_name_plural = _('국적')
        db_table = 'Nationality'
        ordering = ['code']
