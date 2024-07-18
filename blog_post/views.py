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
import requests

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
    
    house_info_list = data["data"]
    top_data_list=house_info_list["topData"]
    
    
    # print('hello',top_data_list)
    
    # first_data = getFirstBuildInfoFromTable()
    # build_name=first_data.build_name
    # cover=first_data.cover 
    # line_notify(build_name=build_name,cover=cover)
    
    for x in top_data_list:
        save_house_info(x)
    
    text= json.dumps(data)
    
    return HttpResponse(text)


"""將一筆房屋資訊加進table裡"""
def addToTable(build_info):
    try:
        to_added_info={}

        for field in BuildInfo._meta.get_fields():
            if(field.name!='id'):
                to_added_info[field.name]=build_info[field.name]  
        
        BuildInfo.objects.create(**to_added_info)
        
    except Exception as Err:
        traceback.print_exception(Err)
        
 
 
 
        
"""
取得buildinfo Table 的 第2筆資料
todo 可能會改寫
"""        
def getFirstBuildInfoFromTable():
   return BuildInfo.objects.get(id=2)


# line 通知
def line_notify(build_name,cover):
    # token 之後要抽離到設定檔
    token = 'uRt31oA2Uw5HiRVEjwHuI1BhlkpzEvQG8zWL03kHXyw'  # 填入你的token
    url = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': 'Bearer ' + token
    }
    data = {
        'message': build_name
    }
    
    local_image_path = "downloaded_image.jpg"
    download_image(cover, local_image_path)
     
    files = {
        "imageFile": open(local_image_path, "rb")
    }
    
    requests.post(url, headers=headers, data=data,files=files)

        
# 下載圖片 因為open只能用本機檔案傳遞
def download_image(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
    else:
        raise Exception("Failed to download image")
    
    

from django.db import transaction

# 假設你已經在 models.py 中定義了對應的模型
from .models import HouseInfo, Photo, RentTag, Surrounding

##新增住屋資訊進去table

def save_house_info(data):
    with transaction.atomic():  # 使用事務確保數據一致性
        # 創建 Surrounding 實例
        surrounding_data = data.pop('surrounding')
        surrounding = Surrounding.objects.create(**surrounding_data)
        
        # 創建 Property 實例，不包含多對多字段
        property_data = {
            'title': data['title'],
            'type': data['type'],
            'post_id': data['post_id'],
            'price': data['price'],
            'price_unit': data['price_unit'],
            'section_name': data['section_name'],
            'street_name': data['street_name'],
            'area': data['area'],
            'community': data['community'],
            'room_str': data['room_str'],
            'is_video': data['is_video'],
            'preferred': data['preferred'],
            'kind': data['kind'],
            'surrounding': surrounding  # 一對一關聯
        }
        
        
        property_instance, created = HouseInfo.objects.update_or_create(
            post_id=data['post_id'],
            defaults=property_data
        )
        
        
        # 處理照片列表
        property_instance.photo_list.clear()
        for photo_url in data['photo_list']:
            photo, _ = Photo.objects.get_or_create(url=photo_url)
            property_instance.photo_list.add(photo)
        
        # 處理租賃標籤
        property_instance.rent_tag.clear()
        for tag_data in data['rent_tag']:
            tag, _ = RentTag.objects.get_or_create(id=tag_data['id'], defaults={'name': tag_data['name']})
            property_instance.rent_tag.add(tag)
        
        # 保存 Property 實例
        property_instance.save()


