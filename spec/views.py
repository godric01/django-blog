# -*- coding: UTF-8 -*-

from django.utils.translation import ugettext as _
from spec.models import Category, Specification
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import get_object_or_404,get_list_or_404,render_to_response
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    categorys = Category.objects.all()

    return render_to_response('spec/index.html',
                              {'categorys':categorys,
                            'tab':'spec'})
