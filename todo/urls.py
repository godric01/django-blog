from django.conf.urls.defaults import *
urlpatterns = patterns('todo.views',                       
    url(r'^$','index',name='todo'),
#    (r'^task/add/', 'task_add'),
#    (r'^task/done/','task_done'),
#    (r'^task/undone/','task_undone'),
#    (r'^task/delete/','task_del'),
#    (r'^project/add/', 'project_add'),
#    (r'^project/delete/', 'project_del'),
#    (r'^project/change_type/', 'project_chg_type'),                        
)