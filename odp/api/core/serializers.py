from rest_framework import serializers
from odp.apps.core.models import Team, Player


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'team_id', 'rating', 'wins', 'losses', 'last_match_time', 'name',
                  'tag', 'logo_url']


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name',)


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['team_id', 'email', 'phone_number', 'full_name',
                  'open_dota_account_id', 'solo_competitive_rank', 'competitive_rank',
                  'rank_tier', 'leaderboard_rank', 'steamid', 'avatar', 'loccountrycode']


class PlayerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['email', 'phone_number', 'full_name', 'open_dota_account_id']
