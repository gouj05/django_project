from django.db import models

# Create your models here.
class Categories(models.Model):
    title= models.CharField(max_length=50)
    image=models.ImageField(upload_to="category")
    class Meta:
        verbose_name_plural="Categories"

    def __str__(self):
       return self.title 

class News(models.Model):
    category=models.ForeignKey(Categories, on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    detail=models.TextField()
    image1=models.ImageField(upload_to="news/")
    image2=models.ImageField(upload_to="news/",blank=True,null=True)
    published=models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.title


    class Meta:
        verbose_name_plural="News"

   


    