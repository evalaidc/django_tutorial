# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# when using shortcut you don't have to use template loader -- instead can use the .shortcuts import render above
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    ## shortcut when render is imported
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("question %s." % question_id)

def results(request, question_id):
    response = "Results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Votes of question %s." % question_id)
