from rest_framework import serializers
from odp.apps.core.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'team_id', 'rating', 'wins', 'losses', 'last_match_time', 'name',
                  'tag', 'logo_url']


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name',)
