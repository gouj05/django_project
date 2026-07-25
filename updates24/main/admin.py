from django.contrib import admin
from .models import *
# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    list_display=["title","image"]
class NewsAdmin(admin.ModelAdmin):
    list_display=["category","title","detail","image1","image2","published"]
# Register your models here.
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(News,NewsAdmin)
