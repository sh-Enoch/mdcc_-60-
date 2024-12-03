from django.shortcuts import render, HttpResponse, redirect
from .models import BlogPost    
from .forms import BlogPostForm
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


def profile(request):
    return render(request, 'blogpost/profile.html')


def new_blog(request):
    form = BlogPostForm()
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('popular')
        
    context = {
        "form": form,
    }
    return render(request, 'blogpost/new_blog.html', context)