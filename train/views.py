#coding=utf-8
from django.utils.translation import ugettext as _
from train.models import Project,Task
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import get_object_or_404,get_list_or_404,render_to_response
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    projects = Project.objects.all()
    
    return render_to_response('todo/index.html',
                              {'projects':projects,
                            'tab':'todo'})
    #return HttpResponse('this a test task page')
