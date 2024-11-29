from django.shortcuts import render, HttpResponse
from .models import BlogPost    
# Create your views here.

def home(request):
    context = {
        "name": "Django Blog",
    }
    return render(request, 'blogpost/index.html', context)

def blog(request):
    
    return HttpResponse('This is the blog page.')

def about(request):
    return render(request, 'blogpost/about.html')

def popular(request):
    blogs  = BlogPost.objects.all()
    context = {
        "blogs": blogs,
    }

    return render(request, 'blogpost/popular.html', context)