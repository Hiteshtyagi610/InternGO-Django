from django.urls import path 
from . import views

urlpatterns = [
   
    path('detail/', views.detail,name='detail'),

    path('post/', views.post,name='post'),
    path('', views.internship_list, name='internship_list'),

]