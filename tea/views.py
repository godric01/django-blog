#coding=utf-8
from django.utils.translation import ugettext as _
from tea.models import Topic
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import get_object_or_404,get_list_or_404,render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from django.template import loader,Context,RequestContext


PAGE_SIZE = 20

def index(request):
    topics = Paginator(Topic.objects.all(), PAGE_SIZE)
    pageid = int(request.GET.get('page', '1'))
    currentTopicPage = topics.page(pageid)  
    if request:
        context = RequestContext(request)
    return render_to_response('tea/index.html',
                              {'topics':currentTopicPage,
                            'tab':'tea'},context_instance=context)

def topic_add(request):    
    topic = Topic()
    topic.topic_name = request.POST.get('topic_name')
    topic.topic_publisher = request.POST.get('topic_publisher')
    topic.topic_email = request.POST.get('topic_email')
    topic.save()
    return HttpResponse('success')