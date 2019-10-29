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
