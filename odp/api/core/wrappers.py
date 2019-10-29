import requests


class OpenDotaClient:
    BASE_URL = 'https://api.opendota.com/api/'

    def __init__(self):
        self.session = requests.session()

    def get_team_by_name(self, team_name):
        result = self.session.get(self.BASE_URL + 'teams/')
        if result.status_code == 200:
            for team_dict in result.json():
                if team_dict['name'] == team_name:
                    return team_dict
            return None
        raise result.raise_for_status()

    def get_player_by_account_id(self, account_id):
        result = self.session.get(self.BASE_URL + 'players/{}'.format(account_id))
        if result.status_code == 200:
            if "profile" in result.json():
                player_data = result.json()
                player = {
                    'solo_competitive_rank': player_data['solo_competitive_rank'],
                    'competitive_rank': player_data['competitive_rank'],
                    'rank_tier': player_data['rank_tier'],
                    'leaderboard_rank': player_data['leaderboard_rank'],
                    'steamid': player_data['profile']['steamid'],
                    'avatar': player_data['profile']['avatar'],
                    'loccountrycode': player_data['profile']['loccountrycode'],
                }
                return player
            return None
        raise result.raise_for_status()
