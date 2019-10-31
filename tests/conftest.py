import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from odp.apps.core.models import Team


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


@pytest.fixture()
def create_team(db):
    return Team.objects.create(team_id=1111, rating=1.1, wins=2, losses=2,
                               last_match_time=1234, name="TestTeam", tag="TT",
                               logo_url="https://fake.png")
