from django.test import TestCase
from ..forms import PostForm
from ..models import Category


class TestForm(TestCase):
    def test_post_form_with_valid_data(self):
        obj_category = Category.objects.create(name='hello')
        context = {
            'category': obj_category,
            'title': 'Test Title',
            'content': 'Test Content',
            'status': True,
        }
        form = PostForm(data=context)
        self.assertTrue(form.is_valid())

    def test_post_form_with_valid_no_data(self):
        context = {}
        form = PostForm(data=context)
        self.assertFalse(form.is_valid())
