import pytest


@pytest.mark.django_db
def test_get_teams_list(create_team, api_client_auth_user):
    response = api_client_auth_user.get('/api/teams/')
    assert response.status_code == 200
    assert type(response.json()) == list
    assert response.json()[0]['team_id'] == 1111


@pytest.mark.django_db
def test_get_teams_empty_list(api_client_auth_user):
    response = api_client_auth_user.get('/api/teams/')
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0
