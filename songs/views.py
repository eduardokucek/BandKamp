from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework.generics import ListCreateAPIView
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


class SongView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer

    @extend_schema(
        description="Rota para listagem de músicas",
        summary="Lista música por ID",
        tags=["Criação e listagem de músicas"],
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        description="Rota para criação de música",
        summary="Cria música",
        tags=["Criação e listagem de músicas"],
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Song.objects.all()
        return Song.objects.all()

    @extend_schema(
        tags=["Criação e listagem de músicas"],
    )
    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs.get("pk"))
        serializer.save(album=album)
