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
        
    class Meta:
        ordering = ['-req_time']
   
    def __str__(self):
        return self.name
