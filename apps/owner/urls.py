from django.urls import path
from . import views


urlpatterns = [
     path('owner_list/', views.owner_list, name='owner_list'),
     path('', views.owner_details, name='owner_detail'),
     path('owner_search/', views.owner_search, name='owner_search'),
     path('owner_create/', views.owner_create, name='owner_create'),
     path('delete_owner/(?P<id>[0-9]+)/$', views.owner_delete, name='owner_delete'),
     path('edit_owner/(?P<id>[0-9]+)/$', views.owner_edit, name='owner_edit'),

     # URLs para nuestras vistas basadas en clases.
     path('owner_list_vc/', views.OwnerList.as_view(), name='owner_list_vc'),
     path('owner_create_vc/', views.OwnerCreate.as_view(), name='owner_create_vc'),
     path('edit_owner_vc/(?P<pk>[0-9]+)/$', views.OwnerUpdate.as_view(), name='owner_edit_vc'),
     path('delete_owner_vc/(?P<pk>[0-9]+)/$', views.OwnerDelete.as_view(), name='owner_delete_vc'),
]

