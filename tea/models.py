#coding=utf-8
from django.utils.translation import ugettext as _
from django.db import models

class Topic(models.Model):
    topic_name = models.CharField(_('Topic Name'),max_length=255)
    topic_publisher = models.CharField(_('Topic Publisher'),max_length=10,null=True,blank=True)
    topic_desc = models.TextField(_('Topic Desc'),null=True,blank=True)
    topic_email = models.EmailField(verbose_name=_('Email'))
    topic_plan = models.DateTimeField(_('Plan Date'),null=True,blank=True)
    topic_created = models.DateTimeField(_('Created Date'),auto_now_add=True)
    topic_lastupdated = models.DateTimeField(_('LastUpdated Date'),auto_now=True)
    topic_order = models.IntegerField(_('Order'),default=0,help_text=_('Minimal at front'))
    topic_published = models.BooleanField(_('Topic Published'), default=False)
    topic_completed = models.BooleanField(_('Is topic completed'),default=False)
    
    def __unicode__(self):
        return self.topic_name    
           
    class Meta:
        ordering = ['topic_completed','topic_order']        
        verbose_name=_('Tea Topic')
        verbose_name_plural = _('Tea Topic')
        