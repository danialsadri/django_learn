import requests
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    RedirectView,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import PostForm, PostUpdateForm
from .models import Post
from .tasks import send_email


class TestView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context


class RedirectToDjangoView(RedirectView):
    url = "https://www.djangoproject.com/"
    # pattern_name = 'blog:post-list'
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, id=kwargs.get("pk"))
        print(f"post: {post}")
        return super().get_redirect_url(*args, **kwargs)


class PostListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "blog.view_post"
    model = Post
    # queryset = Post.objects.filter(status=True)
    template_name = "post_list.html"
    context_object_name = "posts"
    paginate_by = 1
    ordering = "-created_at"

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = "post"
    template_name = "post_detail.html"


class PostFormView(LoginRequiredMixin, FormView):
    model = Post
    form_class = PostForm
    template_name = "post_form.html"
    success_url = reverse_lazy("blog:post-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    # fields = ['title', 'content']
    template_name = "post_create.html"
    success_url = reverse_lazy("blog:post-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = "post_update.html"
    success_url = reverse_lazy("blog:post-list")


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("blog:post-list")


def send_email_test(request):
    send_email.delay()
    return HttpResponse('<h1>Done Sending Email</h1>')


def cache_test(request):
    if cache.get('test_api') is None:
        response = requests.get("https://9e1b6e60-172e-4f0c-8501-173a2ed854c6.mock.pstmn.io/test/delay/5").json()
        cache.set('test_api', response)
        return JsonResponse(cache.get('test_api'))
    return JsonResponse(cache.get('test_api'))
