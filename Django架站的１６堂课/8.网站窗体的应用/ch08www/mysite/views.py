#! -*- coding:utf-8 -*-
from django.shortcuts import render

from django.template.loader import get_template
from django.http import HttpResponse

from mysite import models


def index(request):
    template = get_template('index.html')

    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    html = template.render(locals())
    return HttpResponse(html)