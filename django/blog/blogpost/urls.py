from django.urls import path
from .views import home, blog, about, popular, profile, new_blog


urlpatterns = [
    path('landing/', home, name='home'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('popular/', popular, name='popular'),
    path('profile/', profile, name='profile'),
    path('new_blog/', new_blog, name='new_blog'),
]