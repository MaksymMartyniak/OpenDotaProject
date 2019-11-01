import requests_mock
from odp.api.core.wrappers import OpenDotaClient

test_player_data = {
    "profile": {
        "account_id": 12345,
        "steamid": "12345",
        "avatar": "https://fake.png",
        "loccountrycode": "TL"
    },
    "solo_competitive_rank": 1111,
    "competitive_rank": 1111,
    "rank_tier": 1111,
    "leaderboard_rank": 1111
}

test_player_any_data = {}

URL = 'https://api.opendota.com/api/players/{}'.format(
    test_player_data['profile']['account_id']
)


def test_get_player():
    client = OpenDotaClient()
    with requests_mock.mock() as mock:
        mock.get(URL, json=test_player_data)
        res = client.get_player_by_account_id(12345)
        assert res['steamid'] == '12345'
        assert len(res.keys()) == 7


def test_get_no_player():
    client = OpenDotaClient()
    with requests_mock.mock() as mock:
        mock.get(URL, json=test_player_any_data)
        res = client.get_player_by_account_id(12345)
        assert res is None
