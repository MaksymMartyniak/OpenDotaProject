from .serializers import TeamSerializer, TeamCreateSerializer, PlayerSerializer, \
    PlayerCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from odp.apps.core.models import Team
from .wrappers import OpenDotaClient
from rest_framework import status
from rest_framework import serializers


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TeamSerializer
    lookup_url_kwarg = 'team_id'

    def create(self, request, *args, **kwargs):
        serializer = TeamCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = OpenDotaClient()
        team_json = client.get_team_by_name(serializer.validated_data['name'])
        if not team_json:
            raise serializers.ValidationError("Team with this name can't be found")
        serializer = self.get_serializer(data=team_json)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PlayerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlayerSerializer
    lookup_url_kwarg = 'team_id'

    def create(self, request, *args, **kwargs):
        input_data = self.get_validated_input_data()
        client = OpenDotaClient()
        player_data = client.get_player_by_account_id(input_data['open_dota_account_id'])

        if not player_data:
            raise serializers.ValidationError(
                "Player with current account id can't be find"
            )

        input_data.update(player_data)
        serializer = self.get_serializer(data=input_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_validated_input_data(self):
        input_serializer = PlayerCreateSerializer(data=self.request.data)
        input_serializer.is_valid(raise_exception=True)
        input_data = input_serializer.validated_data
        input_data.update(self.kwargs)
        return input_data
