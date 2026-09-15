from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    GenreListAPIView,
    GenreDetailAPIView,
    ActorListAPIView,
    ActorDetailAPIView,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreListAPIView.as_view(), name="genre-list"),
    path(
        "genres/<int:pk>/",
        GenreDetailAPIView.as_view(),
        name="genre-detail"
    ),
    path("actors/", ActorListAPIView.as_view(), name="actor-list"),
    path(
        "actors/<int:pk>/",
        ActorDetailAPIView.as_view(),
        name="actor-detail"
    ),
]

app_name = "cinema"
