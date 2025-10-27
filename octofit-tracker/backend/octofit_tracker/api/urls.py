from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ProfileViewSet
from . import views

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path("health/", views.health, name="health"),
    path("", include(router.urls)),
]
