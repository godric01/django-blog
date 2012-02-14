from django.conf.urls.defaults import *
urlpatterns = patterns('spec.views',
    url(r'^$','index',name='spec'),
)
