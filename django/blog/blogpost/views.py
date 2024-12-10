from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import BlogPost    
from .forms import BlogPostForm, AuthorForm
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse("login")

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
    author_form =  AuthorForm()
    context ={
        "form": author_form,
    }
    return render(request, 'blogpost/profile.html', context)


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