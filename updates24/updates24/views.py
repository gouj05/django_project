from django.shortcuts import render
from main.models import Categories,News

def home(request):
    categories=Categories.objects.all()
    news=News.objects.all()
    return render(request,"index.html",{"categories":categories, "news":news})
def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"index.html")
def search(request):
    q=request.GET.get("data")
    search=News.objects.filter(title__icontains=q)
    return render(request,"search.html",{'search':search})

    