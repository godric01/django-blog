#coding=utf-8
from django.utils.translation import ugettext as _
from django.db import models

#Project types
PROJECT_TYPE = (
    (0,'public'),
    (1,'private')
)
TASK_PRIORITY = (
    (0,'low'),
    (1,'medium'),
    (2,'high')
)

class Project(models.Model):
    '''todo project entity'''
    project_name = models.CharField(_('Project Name'),max_length=255)
    project_created = models.DateTimeField(_('Created Date'),auto_now_add=True)
    project_lastupdated = models.DateTimeField(_('LastUpdated Date'),auto_now=True)
    #project_type = models.IntegerField(_('Project type'),default=0,choices=PROJECT_TYPE)
    #project_desc = models.CharField(_('Project Description'),max_length=1024)
    project_tasks = models.IntegerField(_('Project task count'),default=0)
    #project_completed = models.IntegerField(_('Completed task count'),default=0)
    #project_slug = models.CharField(_('Project slug'),max_length=255)
    project_order = models.IntegerField('Project Order',default=0)
    
    def __unicode__(self):
        return self.project_name    
           
    class Meta:
        ordering = ['-project_order']        
        verbose_name=_('Todo Project')
        verbose_name_plural = _('Todo Projects')
    
class Task(models.Model):
    '''todo task'''
    task_name = models.CharField(_('Task Name'),max_length=255)
    task_project = models.ForeignKey(Project, related_name='task_set',verbose_name=_('Task Project'))
    task_created = models.DateTimeField(_('Created Date'))
    task_lastupdated = models.DateTimeField(_('LastUpdated Date'),auto_now=True)
    #task_priority = models.IntegerField(_('Task Priority'),default=0,choices=TASK_PRIORITY)
    task_completed = models.BooleanField(_('Is task completed'),default=False)
    # SAVE|TODO save function override
    def __unicode__(self):
        return self.task_name
    
    class Meta:
        ordering = ['task_completed','-task_created']
        verbose_name = _('Todo Task')
        verbose_name_plural = _('Todo Tasks')
        