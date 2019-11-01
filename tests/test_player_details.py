import pytest


@pytest.mark.django_db
def test_get_player_details(create_player, api_client_auth_user):
    player = create_player
    response = api_client_auth_user.get(
        '/api/teams/{}/players/{}'.format(player.team_id.id, player.id)
    )

    assert response.status_code == 200
    print(response.json())
    assert response.json()['full_name'] == 'Test Player'


@pytest.mark.django_db
def test_get_no_player_details(create_team, api_client_auth_user):
    team = create_team
    response = api_client_auth_user.get(
        '/api/teams/{}/players/{}'.format(team.id, 0)
    )

    assert response.status_code == 404
    assert response.json()['detail'] == "Not found."
