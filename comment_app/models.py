from django.db import models
from blog_app.models import Blog
# Create your models here.
class Comment(models.Model):
    full_name = models.CharField(max_length=255)
    email= models.EmailField()
    comment = models.TextField()
    blog_id = models.ForeignKey(Blog,on_delete=models.CASCADE)   

    def __str__(self):
        return self.full_name +" : "+ self.email +" : " +self.comment 