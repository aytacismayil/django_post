from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Products(models.Model):
    deyer_secimleri=(
        (1,'bahali'),
        (2,'orta'),
        (3,'ucuz')
    )
    name = models.CharField(max_length=255 )
    price = models.FloatField(default=0)
    images = models.ImageField(upload_to='users')
    deyer = models.PositiveIntegerField(choices=deyer_secimleri)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name + ":" + str(self.price) + "AZN"

    class Meta:
        verbose_name = "Mehsul"
        verbose_name_plural = "Mehsullar"
        unique_together = ("name","price")
 