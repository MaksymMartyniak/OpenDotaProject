import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User


@pytest.fixture()
def create_user(db):
    username = "TestUser"
    password = "12345"
    User.objects.create_user(username=username, password=password)


@pytest.fixture()
@pytest.mark.django_db
def api_client_auth_user(create_user):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token 12345')
    user = User.objects.get(username="TestUser")
    client.force_authenticate(user=user, token="Token 12345")
    return client
