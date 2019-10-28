from rest_framework import serializers
from odp.apps.core.models import Team
from .wrappers import OpenDotaClient


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'team_id', 'rating', 'wins', 'losses', 'last_match_time', 'name',
                  'tag', 'logo_url']


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name',)

    def create(self, validated_data):
        name = validated_data.get('name')
        client = OpenDotaClient()
        team_json = client.get_team_by_name(name)
        if team_json is not None:
            team = Team.objects.create(
                team_id=team_json['team_id'],
                rating=team_json['rating'],
                wins=team_json['wins'],
                losses=team_json['losses'],
                last_match_time=team_json['last_match_time'],
                name=team_json['name'],
                tag=team_json['tag'],
                logo_url=team_json['logo_url'],
            )
            return team
        raise serializers.ValidationError("Team with this name can't be found")
