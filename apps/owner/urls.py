from django.urls import path
from . import views


urlpatterns = [
     path('owner_list/', views.owner_list, name='owner_list'),
     path('', views.owner_details, name='owner_detail'),
     path('owner_search/', views.owner_search, name='owner_search'),
     path('owner_create/', views.owner_create, name='owner_create'),
     path('delete_owner/(?P<id>[0-9]+)/$', views.owner_delete, name='owner_delete'),
]

