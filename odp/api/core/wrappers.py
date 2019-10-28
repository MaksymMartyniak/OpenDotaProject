import requests


class OpenDotaClient:
    BASE_URL = 'https://api.opendota.com/api/'

    def __init__(self):
        self.session = requests.session()

    def get_team_by_name(self, team_name):
        result = self.session.get(self.BASE_URL + 'teams/')
        if result.status_code == 200:
            for dic in result.json():
                if dic['name'] == team_name:
                    return dic
            return None
        raise result.raise_for_status()
