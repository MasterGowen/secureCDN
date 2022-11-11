from django.urls import path, include

from . import views


urlpatterns = (
    path('', views.LibraryListView.as_view(), name='index'),
    path('library/', views.LibraryListView.as_view(), name='library_list'),
    path('library/create/', views.LibraryCreateView.as_view(), name='library_create'),
    path('library/detail/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('library/update/<int:pk>/', views.LibraryUpdateView.as_view(), name='library_update'),
    path('library/delete/<int:pk>/', views.LibraryDeleteView.as_view(), name='library_delete'),
    path('resource/', views.ResourceListView.as_view(), name='resource_list'),
    path('resource/create/', views.ResourceCreateView.as_view(), name='resource_create'),
    path('resource/detail/<int:pk>/', views.ResourceDetailView.as_view(), name='resource_detail'),
    path('resource/update/<int:pk>/', views.ResourceUpdateView.as_view(), name='resource_update'),
    path('resource/delete/<int:pk>/', views.ResourceDeleteView.as_view(), name='resource_delete'),
    path('permissions/', views.PermissionsListView.as_view(), name='permissions_list'),
    path('permissions/create/', views.PermissionsCreateView.as_view(), name='permissions_create'),
    path('permissions/detail/<int:pk>/', views.PermissionsDetailView.as_view(), name='permissions_detail'),
    path('permissions/update/<int:pk>/', views.PermissionsUpdateView.as_view(), name='permissions_update'),
    path('permissions/delete/<int:pk>/', views.PermissionsDeleteView.as_view(), name='permissions_delete'),
)
