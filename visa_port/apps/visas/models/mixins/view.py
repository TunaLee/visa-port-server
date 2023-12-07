# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Choices
from superclub.modules.choices import STAFF_TYPE_CHOICES


class VisaViewMixin(models.Model):
    # Operation Manager Permission
    recent_view_date = models.DateField(_('비자 최근 조회일'), null=True, blank=True)

    class Meta:
        abstract = True
