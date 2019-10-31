import pytest
from unittest import mock
from odp.api.core.wrappers import OpenDotaClient

pytestmark = pytest.mark.django_db
test_team_data = {
    "team_id": 1234,
    "rating": 1234.67,
    "wins": 123,
    "losses": 34,
    "last_match_time": 1566733817,
    "name": "abc",
    "tag": "abc",
    "logo_url": "https://fake.png"
}


@mock.patch.object(
    OpenDotaClient, 'get_team_by_name',
    return_value=test_team_data
)
def test_team_creation(get_team_by_name, api_client_auth_user):
    response = api_client_auth_user.post('/api/teams/', {'name': 'abc'}, format='json')
    assert response.status_code == 201
    assert response.json()['name'] == 'abc'


@mock.patch.object(
    OpenDotaClient, 'get_team_by_name',
    return_value=None
)
def test_team_no_creation(get_team_by_name, api_client_auth_user):
    response = api_client_auth_user.post('/api/teams/', {'name': 'abc'}, format='json')
    print(response.json())
    assert response.status_code == 400
    assert response.json() == ["Team with this name can't be found"]
