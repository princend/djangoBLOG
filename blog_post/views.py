from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog_post.models import Post
# Create your views here.
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from libraries.service.get591 import Get591byAPiService
import json
from blog_post.models import BuildInfo
import traceback

def index(requests):
    posts = Post.objects.all()
    # post_list = list()
    # for count, post in enumerate(posts):
    #     post_list.append("<h2>#{}: {}</h2> <br><hr>".format(str(count), str(post)))
    #     post_list.append("<small> {} </small> <br> <br>".format(post.content))
    now = datetime.now()
    
    return render(requests,"pages/index.html",locals())


def showPost(requests, slug):
    try:
        # 左邊的slug為資料庫的欄位(key),右邊的slug為django傳進來的slug參數
        post = Post.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return redirect('/')
    except MultipleObjectsReturned:
        return redirect('/')
    
    # return HttpResponse(slug)
    return render(requests, "pages/post.html", locals())


def get591_view(request):
    service =  Get591byAPiService()
    data=  service.getInfo()
    
    build_info_list=data["data"]
    
    
    # for x in build_info_list:
    #     addToTable(x)
    
    # print(qq)
    text= json.dumps(data)
    # addToTable()
    return HttpResponse(text)

"""加進table裡"""
def addToTable(build_info):

    try:
        to_added_info={}

        for field in BuildInfo._meta.get_fields():
            if(field.name!='id'):
                to_added_info[field.name]=build_info[field.name]  
        
        BuildInfo.objects.create(**to_added_info)
        
    except Exception as Err:
        traceback.print_exception(Err)