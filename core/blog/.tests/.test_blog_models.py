from django.test import TestCase
from ..models import Post, Category
from accounts.models import Profile, User


class TestModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.user = User.objects.create_user(email='test@test.com', password='Aa.123456')
        self.profile = Profile.objects.create(user=self.user, first_name='John', last_name='Doe')

    def test_post_create_valid_data(self):
        post = Post.objects.create(
            author=self.profile,
            category=self.category,
            title='Test Title',
            content='Test Content',
            status=True,
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEquals(post.title, 'Test Title')
