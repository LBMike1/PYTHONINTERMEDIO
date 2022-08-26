from django.urls import path
from . import views

urlpatterns = [
     path('owner_list/', views.owner_list, name='post_list'),
     path('', views.owner_details, name='owner_detail'),
     path('owner_search/', views.owner_search, name='owner_search'),
]

