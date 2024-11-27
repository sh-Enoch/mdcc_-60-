from  django.urls import path
from .views import shelter_list, shelter_detail


urlpatterns = [
    path('', shelter_list, name='shelter_list'),
    path('shelter/<int:pk>', shelter_detail, name='shelter_detail'),

]