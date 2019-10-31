import pytest
from unittest import mock
from odp.api.core.wrappers import OpenDotaClient

pytestmark = pytest.mark.django_db


@mock.patch.object(
    OpenDotaClient, 'get_team_by_name',
    return_value={
        "team_id": 1234,
        "rating": 1234.67,
        "wins": 123,
        "losses": 34,
        "last_match_time": 1566733817,
        "name": "abc",
        "tag": "abc",
        "logo_url": "https://fake.png"
    }
)
def test_team_creation(get_team_by_name, api_client_auth_user):
    response = api_client_auth_user.post('/api/teams/', {'name': 'abc'}, format='json')
    print("Response", response.json())
    assert response.status_code == 201
