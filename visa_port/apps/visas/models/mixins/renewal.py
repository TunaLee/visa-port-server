# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

class VisaRenewalMixin(models.Model):
    # Operation Manager Permission
    recent_renewal_date = models.DateField(_('비자 최근 갱신일'), null=True, blank=True)
    exisiting_expiration_date = models.DateField(_('이전 만료일'), null=True, blank=True)

    class Meta:
        abstract = True
