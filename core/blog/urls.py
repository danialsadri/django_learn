from django.urls import path, include
from . import views

app_name = "blog"
urlpatterns = [
    path("test/", views.TestView.as_view(), name="test"),
    path(
        "go-to-django/<int:pk>/",
        views.RedirectToDjangoView.as_view(),
        name="go-to-django",
    ),
    path("post-list/", views.PostListView.as_view(), name="post-list"),
    path("post-detail/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post-form/", views.PostFormView.as_view(), name="post-form"),
    path("post-create/", views.PostCreateView.as_view(), name="post-create"),
    path("post-update/<int:pk>/", views.PostUpdateView.as_view(), name="post-update"),
    path("post-delete/<int:pk>/", views.PostDeleteView.as_view(), name="post-delete"),
    path("send-email-test/", views.send_email_test, name="send-email-test"),
    path("api/v1/", include("blog.api.v1.urls")),
]
