from django.urls import path
from .views import show_url

urlpatterns = [
    path("<str:code>/", show_url),
]