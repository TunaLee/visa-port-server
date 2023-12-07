# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from com_duck.bases.models import Model


class Board(Model):
    category = models.ForeignKey('categories.Category', related_name='boards', on_delete=models.CASCADE)
    category_name = models.CharField(_('카테고리 이름'), max_length=60, null=True, blank=True)

    name = models.TextField(blank=True, null=True, verbose_name=_('게시판 명'))

    class Meta:
        verbose_name = verbose_name_plural = _('게시판')
        db_table = 'board'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super(Board, self).save(*args, **kwargs)

        # Set category name
        self.category_name = self.category.name
