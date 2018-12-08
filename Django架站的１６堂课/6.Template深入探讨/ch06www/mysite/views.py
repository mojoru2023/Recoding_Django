from django.shortcuts import render

# Create your views here.


from django.template.loader import get_template

from django.http import HttpResponse
from datetime import datetime


def index(request,tvno='0'):
    tv_list = {{'name':'CCTV News','tvcode':'YPHFG2I0DEO'},
               {'name':'CCTV 中文国际','tvcode':'E1DTZBY4XR4'}}

    template = get_template('index.html')
    now = datetime.now()
    tvno = tvno
    tv = tv_list[int(tvno)]

    html = template.render(locals())
    return HttpResponse(html)




