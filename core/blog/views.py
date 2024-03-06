from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, PostUpdateForm


class TestView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'
        context['posts'] = Post.objects.all()
        return context


class RedirectToDjangoView(RedirectView):
    url = 'https://www.djangoproject.com/'
    # pattern_name = 'blog:post-list'
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


class PostFormView(FormView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('blog:post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # fields = ['title', 'content']
    template_name = 'post_create.html'
    success_url = reverse_lazy('blog:post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'post_update.html'
    success_url = reverse_lazy('blog:post-list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog:post-list')
