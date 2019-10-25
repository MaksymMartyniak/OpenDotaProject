from django.urls import path
from .views import Login


urlpatterns = [
    path('obtain-token/', Login.as_view()),
]
