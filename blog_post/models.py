from django.db import models

"""_summary_
Returns:
    _type_: _description_
"""
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)


    class Meta:
        ordering = ['-pub_date']
   
    def __str__(self):
        return self.title


"""_summary
Returns:
    _type_: _description_
"""
class Guestbook(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    req_time = models.DateTimeField(auto_now_add = True)
        
    # +代表升序
    # -代表降序
    class Meta:
        ordering = ['-req_time']
   
    def __str__(self):
        return self.name


# 591房屋資訊
class BuildInfo(models.Model):
    hid = models.IntegerField(unique=True)
    build_name = models.CharField(max_length=255)
    cover = models.URLField(max_length=500)
    price = models.CharField(max_length=50)
    price_num = models.CharField(max_length=50)
    price_unit = models.CharField(max_length=50)
    browsenum = models.CharField(max_length=50)
    section_name = models.CharField(max_length=100)
    region_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    callnum = models.IntegerField()
    area = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
    photo_num = models.IntegerField()
    build_type = models.CharField(max_length=50)
    build_type_val = models.IntegerField()
    purpose = models.CharField(max_length=50)
    purpose_other2_str = models.CharField(max_length=100)
    tag = models.CharField(max_length=255)
    layout = models.CharField(max_length=255)
    build_url = models.URLField(max_length=500)
    tag_type = models.IntegerField()

    def __str__(self):
        return self.build_name