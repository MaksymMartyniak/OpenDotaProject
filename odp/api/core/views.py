from .serializers import TeamSerializer
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

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        client = OpenDotaClient()
        team_json = client.get_team_by_name(name)
        if team_json is not None:
            serializer = self.get_serializer(data=team_json)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        raise serializers.ValidationError("Team with this name can't be found")
