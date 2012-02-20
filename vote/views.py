# -*- coding: UTF-8 -*-

from django.utils.translation import ugettext as _
from vote.models import Category, Vote, VoteLog
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import get_object_or_404,get_list_or_404,render_to_response
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    categorys = Category.objects.all()

    return render_to_response('vote/index.html',
                              {'categorys':categorys,
                            'tab':'vote'})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def submit(request):
    vote_ip = get_client_ip(request)
    vote_type = int(request.POST.get('type'))
    vote_id = int(request.POST.get('id'))
    if vote_id:
        vote = get_object_or_404(Vote,pk=vote_id)

    if vote:
        ip_vote_log = vote.votes_set.all().filter(vote=vote,vote_ip=vote_ip)
        if ip_vote_log:
            return HttpResponse("ip")
        else:
            vote_log = VoteLog(vote=vote,vote_ip=vote_ip)
            vote_log.save()

        if vote_type:
            vote.vote_approve = vote.vote_approve + 1
        else:
            vote.vote_disapprove = vote.vote_disapprove + 1

        vote.save()
    else:
        raise Http404

    return HttpResponse("ok")
