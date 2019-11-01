from odp.api.core.wrappers import OpenDotaClient
import requests_mock

URL = 'https://api.opendota.com/api/teams/'
test_team_data = {
    "team_id": 1234,
    "rating": 1.2,
    "wins": 1,
    "losses": 1,
    "last_match_time": 1111,
    "name": "TestTeam",
    "tag": "TT",
    "logo_url": "https://fake.png"
}


def test_get_team():
    client = OpenDotaClient()
    with requests_mock.mock() as mock:
        mock.get(URL, json=[test_team_data])
        res = client.get_team_by_name('TestTeam')
        assert len(res) == 8
        assert res['team_id'] == 1234


def test_get_fake_team():
    client = OpenDotaClient()
    with requests_mock.mock() as mock:
        mock.get(URL, json=[test_team_data])
        res = client.get_team_by_name('FakeTestTeam')
        assert res is None
