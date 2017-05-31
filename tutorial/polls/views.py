# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("question %s." % question_id)

def results(request, question_id):
    response = "Results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Votes of question %s." % question_id)
