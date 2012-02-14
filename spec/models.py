# -*- coding: UTF-8 -*-

from django.utils.translation import ugettext as _
from django.db import models

class Category(models.Model):
    category_name = models.CharField(_('Category Name'),max_length=255)
    category_order = models.IntegerField(_('Order'),default=0, help_text=_('Minimal at front'))

    def __unicode__(self):
        return self.category_name

    class Meta:
        ordering = ['-category_order']
        verbose_name = verbose_name_plural =_('Category Specification')

class Specification(models.Model):
    spec_name = models.CharField(_('Spec Name'),max_length=255)
    spec_category = models.ForeignKey(Category, related_name='spec_set',verbose_name=_('Category Name'))
    spec_blog_url = models.CharField(_('Spec URL'),null=True,blank=True,max_length=255)
    spec_order = models.IntegerField(_('Order'),default=0, help_text=_('Minimal at front'))

    def __unicode__(self):
        return self.spec_name

    class Meta:
        ordering = ['-spec_order']
        verbose_name = verbose_name_plural = _('Tech Specification')

