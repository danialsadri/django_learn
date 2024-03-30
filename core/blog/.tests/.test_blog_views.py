from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Profile, User
from ..models import Post, Category


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='test@test.com', password='Aa.123456')
        self.profile = Profile.objects.create(user=self.user, first_name='John', last_name='Doe')
        self.category = Category.objects.create(name='Test Category')
        self.post = Post.objects.create(author=self.profile, category=self.category, title='Test Title', content='Test Content', status=True)

    def test_blog_index_url_successful_response(self):
        url = reverse('blog:test')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(str(response.content).find('index'))
        self.assertTemplateUsed(response=response, template_name="index.html")

    def test_blog_post_detail_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse('blog:post-detail', kwargs={'pk': self.post.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_blog_post_detail_anonymous_response(self):
        url = reverse('blog:post-detail', kwargs={'pk': self.post.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)
