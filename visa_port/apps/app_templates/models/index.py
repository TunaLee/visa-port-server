# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from visa_port.bases.models import Model


class Template(Model):

    class Meta:
        verbose_name = verbose_name_plural = _('템플릿')
        db_table = 'visa_port'
        ordering = ['-created']
