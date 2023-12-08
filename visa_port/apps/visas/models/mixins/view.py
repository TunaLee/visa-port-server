# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

class VisaViewMixin(models.Model):
    # Operation Manager Permission
    recent_view_date = models.DateField(_('비자 최근 조회일'), null=True, blank=True)

    expiration_view = models.ForeignKey('views.ExpirationView', null=True)

    class Meta:
        abstract = True
