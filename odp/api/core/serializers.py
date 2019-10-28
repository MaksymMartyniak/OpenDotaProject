from rest_framework import serializers
from odp.apps.core.models import Team
from .wrappers import OpenDotaWrapper


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
        try:
            name = validated_data.get('name')
            team = OpenDotaWrapper()
            team = team.get_team_by_name(name)
            team = Team.objects.create(
                team_id=team['team_id'],
                rating=team['rating'],
                wins=team['wins'],
                losses=team['losses'],
                last_match_time=team['last_match_time'],
                name=team['name'],
                tag=team['tag'],
                logo_url=team['logo_url'],
            )
            team.save()
            return team
        except:
            raise serializers.ValidationError("Team with this name can't be found")
