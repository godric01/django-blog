from django.conf.urls.defaults import *
urlpatterns = patterns('vote.views',
    url(r'^$','index',name='vote'),
    (r'^submit/$', 'submit'),
)
