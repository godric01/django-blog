from django.conf.urls.defaults import *
urlpatterns = patterns('tea.views',                       
    url(r'^$','index',name="tea"),
    url(r'^(?P<pagename>\w+)/$','index',name='page'),
)