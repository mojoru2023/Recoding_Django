from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.core.urlresolvers import reverse

def homepage(request):
    year = 2018
    month = 12
    day = 6
    postid = 1

    html = "<a href='{}'>Show the Post</a>".format('post-url',args=(year,month,day,postid))
    return HttpResponse(html)

# def homepage(request):
#     return HttpResponse('Hello World!')


def about(request,author_no):  # 不要忘记第二个参数

    html = "<h2>Here is Author:{}'s about page!</h2><hr>".format(author_no)
    return HttpResponse(html)


def listing(request,list_date):

    html = "<h2>List Date is {}</h2><hr>".format(list_date)
    return HttpResponse(html)


def post(request,yr,mon,day,post_num):
    # html = '<h2>Post Data is {}</h2><hr>'.format(post_data)
    html = '<h2>{}/{}/{}:Post Number:{}</h2><hr>'.format(yr,mon,day,int(post_num))
    return HttpResponse(html)