import pytest


@pytest.mark.django_db
def test_team_details(create_team, api_client_auth_user):
    team = create_team
    response = api_client_auth_user.get('/api/teams/{}'.format(team.id))
    assert response.status_code == 200
    assert response.json()['id'] == team.id
    assert response.json()['name'] == 'TestTeam'


@pytest.mark.django_db
def test_team_any_details(create_team, api_client_auth_user):
    team = create_team
    response = api_client_auth_user.get('/api/teams/{}'.format(0))
    assert response.status_code == 404
    assert response.json()['detail'] == 'Not found.'
