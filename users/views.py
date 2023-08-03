from rest_framework.views import APIView, Request, Response, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner

from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        description="Rota para listagem de usuários",
        summary="Lista usuários",
        tags=["Criação e listagem de usuários"],
    )
    def get(self, request):
        return self.list(request)

    @extend_schema(
        description="Rota para criação de álbuns.",
        summary="Cria usuário",
        tags=["Criação e listagem de usuários"],
    )
    def post(self, request):
        return self.create(request)


class UserRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        description="Rota para listagem de usuários por ID",
        summary="Lista usuário por ID",
        tags=["Listagem, atualização e deleção de usuários"],
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        description="Rota para atualização de usuários por ID",
        summary="Atualiza usuário por ID",
        tags=["Listagem, atualização e deleção de usuários"],
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        description="Rota para deleção de usuários por ID",
        summary="Deleta usuário por ID",
        tags=["Listagem, atualização e deleção de usuários"],
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
