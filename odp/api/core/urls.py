from django.urls import path
from rest_framework.authtoken import views
from .views import GetAndAddTeams, TeamDetails, AddPlayerInfo


urlpatterns = [
    path('obtain-token/', views.obtain_auth_token),
    path('teams/', GetAndAddTeams.as_view()),
    path('teams/<int:team_id>/', TeamDetails.as_view()),
    path('teams/<int:team_id>/players/', AddPlayerInfo.as_view()),
]
