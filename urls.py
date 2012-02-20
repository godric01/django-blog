from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

from blog import feeds
from blog.models import Post

admin.autodiscover()

# Info for feeds.
feed_dict = {
    'rss': feeds.RssLatestPosts,
    'atom': feeds.AtomLatestPosts,
}
info_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'pubdate',
}
urlpatterns = patterns('',
    #('^admin/(.*)', admin.site.root),
    ('^admin/', include(admin.site.urls)),
    url(r'^utils/vcode/$', 'utils.validatecode.get_validatecode_img', name='validate_code'),
)

# url for static
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_PATH}),
    )
#urls for wap
urlpatterns += patterns('',
    (r'^wap/*',include('wap.urls')),
    #wap pre url
    url(r'wap','wap.views.index',name='wap_pre'),
)

urlpatterns += patterns('',
    (r'^train/*', include('train.urls'))
)

urlpatterns += patterns('',
    (r'tea/*', include('tea.urls'))
)

urlpatterns += patterns('',
    (r'spec/*', include('spec.urls'))
)

urlpatterns += patterns('',
    (r'vote/*', include('vote.urls'))
)

# url for filemanager
urlpatterns += patterns('',
    url(r'^filemanager/(?P<p>.*)$','filemanager.views.index',name='filemanager'),
)
#urls for feeds
urlpatterns += patterns('',
    url(r'^feeds/(?P<url>.*)/$','django.contrib.syndication.views.feed', {'feed_dict':feed_dict},name='feeds'),
    url(r'^rpc/$','blog.rpc.call',name='rpc'),
)
# urls for blog
urlpatterns += patterns('blog.views',
    (r'^$', 'index'),
    #tags
    url(r'^tags/$','tags',name='tags'),
    url(r'^tags/(?P<tagname>.*)/$','tags',name='tagname'),
    url(r'^(\d{4})/(\d{1,2})/(\d{1,2})/(?P<postname>[^/]+)/$','post',name='post_name'),
    #ajax
    url(r'^post/(?P<postid>(\d+))/comment$','post_comment',name='post_comment'),
    #url(r'^post/(?P<postid>(\d+))/comments', 'get_post_comments', name='ajax_post_comments'),
    #category view
    url(r'^category/(?P<catid>\d+)/$','categoryView',name="category_id"),
    url(r'^category/(?P<catname>[^/]+)/$','categoryView',name="category_name"),
    (r'^(?P<year>\d{4})/(?P<month>(\d{1,2})?)/?(?P<date>(\d{1,2})?)/?$','dateposts'),
    url(r'^(?P<pagename>\w+)/$','page',name='page'),
    url(r'^(.+?)(?P<pagename>\w+)/$','page',name='page'),
)
