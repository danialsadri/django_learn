from django.urls import path
from . import views

app_name = 'api-v1'
urlpatterns = [
    path('post-list/', views.post_list, name='post-list'),
    path('post-detail/<int:pk>/', views.post_detail, name='post-detail'),
    path('post-create/', views.post_create, name='post-create'),
    path('post-update/<int:pk>/', views.post_update, name='post-update'),
    path('post-delete/<int:pk>/', views.post_delete, name='post_delete'),
]
