from .serializers import TeamSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import requests
import json
from odp.apps.core.models import Team
from django.shortcuts import get_object_or_404


class GetAndAddTeams(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request):
        result = requests.get('https://api.opendota.com/api/teams')
        data = json.loads(request.body.decode('utf8'))
        data_list = list(filter(lambda di: di['name'] == data['name'], result.json()))
        if len(data_list) == 0:
            return Response("Incorrect team name", status=status.HTTP_400_BAD_REQUEST)
        serializer = TeamSerializer(data=data_list[0])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, team_id):
        team = requests.get(
            'https://api.opendota.com/api/teams/{}'.format(team_id)).json()
        # check whether team dict is empty 404
        serializer = TeamSerializer(team)
        return Response(serializer.data)


class AddPlayerInfo(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body.decode('utf8'))
