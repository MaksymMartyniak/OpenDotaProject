import requests


class OpenDotaWrapper:
    BASE_URL = 'https://api.opendota.com/api/'

    def __init__(self):
        self.session = requests.session()

    def get_team_by_name(self, team_name):
        result = self.session.get(self.BASE_URL + 'teams/')
        for dic in result.json():
            if dic['name'] == team_name:
                return dic
