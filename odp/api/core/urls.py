from django.urls import path
from odp.api.core.views import Login


urlpatterns = [
    path('obtain-token/', Login.as_view()),
]
