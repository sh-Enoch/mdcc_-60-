from django.urls import path
from .views import home, blog, about, popular


urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('popular/', popular, name='popular'),
]