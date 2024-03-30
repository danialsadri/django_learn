import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from accounts.models import Profile, User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(email='test@test.com', password='Aa.123456')
    profile = Profile.objects.create(user=user, first_name='John', last_name='Doe')
    return user


@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_200_status(self, api_client, common_user):
        url = reverse("blog:api-v1:post-list")
        api_client.force_login(user=common_user)
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_403_status(self, api_client, common_user):
        url = reverse("blog:api-v1:post-create")
        data = {
            'title': 'Test Title',
            'content': 'Test Content',
            'status': True,
        }
        response = api_client.post(url, data)
        assert response.status_code == 403

    def test_create_post_response_201_status(self, api_client, common_user):
        url = reverse("blog:api-v1:post-create")
        data = {
            'title': 'Test Title',
            'content': 'Test Content',
            'status': True,
        }
        api_client.force_login(user=common_user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400_status(self, api_client, common_user):
        url = reverse("blog:api-v1:post-create")
        data = {
            'title': 'Test Title',
        }
        api_client.force_login(user=common_user)
        response = api_client.post(url, data)
        assert response.status_code == 400
