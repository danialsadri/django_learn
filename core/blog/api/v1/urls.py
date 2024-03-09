from django.urls import path
from . import views

app_name = 'api-v1'
urlpatterns = [
    # fbv
    path('post-list/', views.post_list, name='post-list'),
    path('post-detail/<int:pk>/', views.post_detail, name='post-detail'),
    path('post-create/', views.post_create, name='post-create'),
    path('post-update/<int:pk>/', views.post_update, name='post-update'),
    path('post-delete/<int:pk>/', views.post_delete, name='post_delete'),
    # cbv
    path('post-list-cbv/', views.PostListView.as_view(), name='post-list-cbv'),
    path('post-detail-cbv/<int:pk>/', views.PostDetailView.as_view(), name='post-detail-cbv'),
    path('post-create-cbv/', views.PostCreateView.as_view(), name='post-create-cbv'),
    path('post-update-cbv/<int:pk>/', views.PostUpdateView.as_view(), name='post-update-cbv'),
    path('post-delete-cbv/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete-cbv'),
    # generic
    path('post-list-create-generic/', views.PostListCreateView.as_view(), name='post-list-create-generic'),
    path('post-retrieve-update-destroy-generic/<int:post_id>/', views.PostRetrieveUpdateDetailView.as_view(), name='post-retrieve-update-destroy-generic'),
]
