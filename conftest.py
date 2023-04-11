import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user() -> User:
    return User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

@pytest.fixture
def api_client_auth(api_client,create_user):
    user = User.objects.get(username='john')
    api_client.force_authenticate(user=user)
    return api_client