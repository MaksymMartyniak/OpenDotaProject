from .serializers import TeamSerializer, TeamCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from odp.apps.core.models import Team


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TeamCreateSerializer
        return TeamSerializer
