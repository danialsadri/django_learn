from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import TestView, PostListView, PostDetailView


class TestUrl(SimpleTestCase):
    def test_blog_test_url_resolve(self):
        url = reverse('blog:test')
        self.assertEquals(resolve(url).func.view_class, TestView)

    def test_blog_list_url_resolve(self):
        url = reverse('blog:post-list')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_blog_detail_url_resolve(self):
        url = reverse('blog:post-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, PostDetailView)
