import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_authentication(create_user):
    client = APIClient()

    response = client.post(
        '/api/obtain-token/',
        {'username': 'TestUser', 'password': '12345'}
    )

    assert len(response.json()['token']) == 40
    assert response.status_code == 200


@pytest.mark.django_db
def test_no_authentication():
    client = APIClient()
    response = client.post(
        '/api/obtain-token/',
        {'username': 'NoTestUser', 'password': '1111'}
    )

    assert response.status_code == 400
    assert response.json()["non_field_errors"] == [
        "Unable to log in with provided credentials."
    ]
