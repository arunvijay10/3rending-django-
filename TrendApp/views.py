from django.shortcuts import render
from .models import Image
from TrendApp.models import *


def TrendView(request):
    return render(request, "trend.html")


def Trending(request):
    cat = Categories.objects.all()
    images = Image.objects.all()
    data = {"images": images,'cat': cat}
    return render(request, "3rend.html", data)


def ArrangeCategory(request,cid):
    cat = Categories.objects.all()
    category= Categories.objects.get(pk=cid)
    images = Image.objects.filter(cat=category)
    data = {"images": images, 'cat': cat}
    return render(request, "3rend.html", data)
