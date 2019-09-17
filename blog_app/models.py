from django.db import models
from author_app.models import Author

 # Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    short_content = models.CharField(max_length=255)
    full_content = models.TextField()
    author_id = models.ForeignKey(Author,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.title +":"+ self.short_content +":"+self.full_content 
        