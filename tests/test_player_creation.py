import pytest
from unittest import mock
from odp.api.core.wrappers import OpenDotaClient

test_player_data = {
    'solo_competitive_rank': 1111,
    'competitive_rank': 1111,
    'rank_tier': 1111,
    'leaderboard_rank': 1111,
    'steamid': 1111,
    'avatar': 'https://fake.png',
    'loccountrycode': 'LC',
}


@mock.patch.object(OpenDotaClient, 'get_player_by_account_id',
                   return_value=test_player_data)
@pytest.mark.django_db
def test_player_creation(get_player_py_account_id, create_team, api_client_auth_user):
    team = create_team
    response = api_client_auth_user.post('/api/teams/{}/players/'.format(team.id),
                                         {
                                             'email': 'testplayer@test.com',
                                             "phone_number": "+380666666699",
                                             'full_name': 'Test Player',
                                             'open_dota_account_id': 1234
                                         }, format='json'
                                         )

    assert response.status_code == 201
    assert response.json()['competitive_rank'] == 1111


@mock.patch.object(OpenDotaClient, 'get_player_by_account_id',
                   return_value=None)
@pytest.mark.django_db
def test_player_no_creation(get_player_py_account_id, create_team, api_client_auth_user):
    team = create_team
    response = api_client_auth_user.post('/api/teams/{}/players/'.format(team.id),
                                         {
                                             'email': 'testplayer@test.com',
                                             "phone_number": "+380666666699",
                                             'full_name': 'Test Player',
                                             'open_dota_account_id': 1234
                                         }, format='json'
                                         )

    assert response.status_code == 400
    assert response.json() == ["Player with current account id can't be find"]
