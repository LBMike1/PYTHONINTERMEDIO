from django.urls import path
from . import views


urlpatterns = [
     path('owner_list/', views.owner_list, name='owner_list'),
     path('', views.owner_details, name='owner_detail'),
     path('owner_search/', views.owner_search, name='owner_search'),
     path('owner_create/', views.owner_create, name='owner_create'),
     path('delete_owner/(?P<id>[0-9]+)/$', views.owner_delete, name='owner_delete'),
     path('edit_owner/(?P<id>[0-9]+)/$', views.owner_edit, name='owner_edit'),

     # URLs para las vistas basadas en clases.
     path('owner_list_vc/', views.OwnerList.as_view(), name='owner_list_vc'),
     path('owner_create_vc/', views.OwnerCreate.as_view(), name='owner_create_vc'),
     path('edit_owner_vc/(?P<pk>[0-9]+)/$', views.OwnerUpdate.as_view(), name='owner_edit_vc'),
     path('delete_owner_vc/(?P<pk>[0-9]+)/$', views.OwnerDelete.as_view(), name='owner_delete_vc'),

     # URLs serializers
     path('owner_list_serializer/', views.ListOwnerSerializer, name="owner_lis_srr"),

     # URLs DJANGO RESTFRAMEWORK
     path('owner_list_drf/', views.OwnerApiView.as_view(), name='owner_list_drf'),
     path('owner_list_drf_def/', views.owner_api_view, name='owner_list_rf_def'),
     path('owner_detail_drf_def/<int:pk>/', views.owner_detail_view, name='owner_detail_rf_def'),
]

