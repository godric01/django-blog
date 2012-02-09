from django.conf.urls.defaults import *
urlpatterns = patterns('train.views',                       
    url(r'^$','index',name='train'),                      
)