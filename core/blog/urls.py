from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('test/', views.TestView.as_view(), name='test'),
    path('go-to-django/<int:pk>/', views.RedirectToDjangoView.as_view(), name='go-to-django'),
    path('post-list/', views.PostListView.as_view(), name='post-list'),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post-form/', views.PostFormView.as_view(), name='post-form'),
    path('post-create/', views.PostCreateView.as_view(), name='post-create'),
]
