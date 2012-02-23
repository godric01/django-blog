# -*- coding: UTF-8 -*-
from django.utils.translation import ugettext as _
from django.db import models

class Project(models.Model):
    project_name = models.CharField(_('Project Name'),max_length=255)
    project_created = models.DateTimeField(_('Created Date'),auto_now_add=True)
    project_lastupdated = models.DateTimeField(_('LastUpdated Date'),auto_now=True)
    project_order = models.IntegerField(_('Order'),default=0,
                                     help_text=_('Minimal at front'))
    
    def __unicode__(self):
        return self.project_name    
           
    class Meta:
        ordering = ['project_order']        
        verbose_name=_('Train Project')
        verbose_name_plural = _('Train Projects')
    
class Task(models.Model):
    task_name = models.CharField(_('Task Name'),max_length=255)
    task_project = models.ForeignKey(Project, related_name='task_set',verbose_name=_('Task Project'))
    task_speaker = models.CharField(_('Task Speaker'),null=True,blank=True,max_length=10)
    task_created = models.DateTimeField(_('Created Date'),null=True,blank=True)
    task_lastupdated = models.DateTimeField(_('LastUpdated Date'),auto_now=True)
    task_completed = models.BooleanField(_('Is task completed'),default=False)

    def __unicode__(self):
        return self.task_name
    
    class Meta:
        ordering = ['task_completed','-task_created']
        verbose_name = _('Train Task')
        verbose_name_plural = _('Train Tasks')
        
