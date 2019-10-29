from django.urls import path
from rest_framework.authtoken import views
from .views import TeamViewSet, PlayerViewSet

urlpatterns = [
    path('obtain-token/', views.obtain_auth_token),
    path('teams/', TeamViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('teams/<int:team_id>', TeamViewSet.as_view({'get': 'retrieve'})),
    path('teams/<int:team_id>/players/', PlayerViewSet.as_view({'post': 'create'})),
]
