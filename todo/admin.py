
from django.contrib import admin
from todo.models import Project, Task

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name','project_tasks','project_created','project_order')    
    search_fields = ['project_name']

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name','task_project','task_completed','task_lastupdated')
    list_filter =('task_project',)        

admin.site.register(Project,ProjectAdmin)
admin.site.register(Task, TaskAdmin)
        
        