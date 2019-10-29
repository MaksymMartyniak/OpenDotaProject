from django.urls import path
from rest_framework.authtoken import views
from .views import TeamViewSet


urlpatterns = [
    path('obtain-token/', views.obtain_auth_token),
    path('teams/', TeamViewSet.as_view({'get': 'list', 'post': 'create'})),
]
