from django.urls import path
from rest_framework.authtoken import views
from .views import TeamViewSet


teams_list = snippet_list = TeamViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


urlpatterns = [
    path('obtain-token/', views.obtain_auth_token),
    path('teams/', teams_list),
]
