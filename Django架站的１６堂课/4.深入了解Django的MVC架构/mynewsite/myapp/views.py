# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404
from myapp.models import Produ
import random
from django.template.loader import get_template







def index(request):
    template = get_template('index.html')
    quotes = ['今日事,今日毕',
              '要收获,先付出',
              '知识就是力量',
              '一个人的个性就是他的命运',
              '你的世界观就是你的世界']
    html = template.render({'quote':random.choice(quotes)})

    return HttpResponse(html)









def disp_detail(request,sku):
    try:
        p = Produ.objects.get(sku=sku)
    except Produ.DoesNotExist:
        raise Http404('找不到指定的产品编号')
    template = get_template('disp.html')
    html = template.render({'product':p})
    return HttpResponse(html)


def listing(request):
    products = Produ.objects.all()
    template = get_template('list.html')
    html = template.render({'products':products})
    return HttpResponse(html)


def about(request):
    template = get_template('about.html')
    html = template.render()
    return HttpResponse(html)

