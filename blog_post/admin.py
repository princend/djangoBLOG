from django.contrib import admin
from blog_post.models import Post,Guestbook


models=[Post,Guestbook]

# Register your models here.
admin.site.register(models)