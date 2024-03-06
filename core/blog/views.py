from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, RedirectView, ListView, DetailView
from .models import Post

class TestView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'
        context['posts'] = Post.objects.all()
        return context


class RedirectToDjangoView(RedirectView):
    url = 'https://www.djangoproject.com/'
    # pattern_name = 'blog:test'
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, id=kwargs.get('pk'))
        print(f'post: {post}')
        return super().get_redirect_url(*args, **kwargs)


class PostListView(ListView):
    model = Post
    # queryset = Post.objects.filter(status=True)
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 1
    ordering = '-created_at'

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostDetailView(DetailView):
    model = Post    
    context_object_name = 'post'
    template_name = 'post_detail.html'
