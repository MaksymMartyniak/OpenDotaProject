import pytest


@pytest.mark.django_db
def test_get_players_list(create_player, api_client_auth_user):
    player = create_player
    response = api_client_auth_user.get(
        '/api/teams/{}/players/'.format(player.team_id.id)
    )

    assert response.status_code == 200
    assert type(response.json()) == list
    assert response.json()[0]['full_name'] == 'Test Player'


@pytest.mark.django_db
def test_get_any_players_list(create_team, api_client_auth_user):
    team = create_team
    response = api_client_auth_user.get(
        '/api/teams/{}/players/'.format(team.id)
    )

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0

