"""
URL configuration for djangoBLOG project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from blog_post.views import index
from blog_post.views import showPost
from blog_post.views import get591_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index),
    
    # 左邊的slug的為型態,右邊的slug 為傳到view function 的變數名稱
    path("post/<slug:slug>/", showPost),
    # 多行
    # path("post/<slug:slug>/<slug2:slug2>/<slug3:slug3>", showPost),
    
    path("test",get591_view)
]
