# -*- coding: UTF-8 -*-

from django.utils.translation import ugettext as _
from django.db import models

class Category(models.Model):
    category_name = models.CharField(_('Category Name'),max_length=255)
    category_desc = models.TextField(verbose_name=_('Description'),null=True,blank=True,default='')
    category_order = models.IntegerField(_('Order'),default=0, help_text=_('Minimal at front'))

    def __unicode__(self):
        return self.category_name

    class Meta:
        ordering = ['-category_order']
        verbose_name = verbose_name_plural =_('Vote Category')

class Vote(models.Model):
    vote_title = models.CharField(_('Vote Title'),max_length=255)
    vote_category = models.ForeignKey(Category, related_name='category_set',verbose_name=_('Vote Category'),null=True,blank=True)
    vote_content = models.TextField(verbose_name=_('Content'),null=True,blank=True,default='')
    vote_approve = models.IntegerField(_('Vote Approve'),default=0)
    vote_disapprove = models.IntegerField(_('Vote Disapprove'),default=0)
    vote_order = models.IntegerField(_('Order'),default=0, help_text=_('Minimal at front'))

    def __unicode__(self):
        return self.vote_title

    class Meta:
        ordering = ['vote_order']
        verbose_name = verbose_name_plural =_('Vote')


class VoteLog(models.Model):
    vote = models.ForeignKey(Vote,verbose_name=_('Vote'),related_name='votes_set')
    vote_ip = models.CharField(_('Vote IP'),max_length=128)
    vote_date = models.DateTimeField(_('Vote Date'),auto_now_add=True)

    class Meta:
        ordering = ['-vote_date']
        verbose_name = verbose_name_plural =_('Vote Log')

