from rest_framework.views import APIView, status, Response
from .models import Album
from .serializers import AlbumSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


class AlbumView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = AlbumSerializer

    @extend_schema(
        description="Rota para listagem de álbuns",
        summary="Lista álbuns",
        tags=["Criação e listagem de albuns"],
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        description="Rota para criação de álbuns",
        summary="Cria álbum",
        tags=["Criação e listagem de albuns"],
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @extend_schema(
        tags=["Criação e listagem de músicas"],
    )
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Album.objects.all()
        return Album.objects.all()

    @extend_schema(
        tags=["Criação e listagem de músicas"],
    )
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
