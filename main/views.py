
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from main.models import Module
from main.paginators import ModulePaginator
from main.serializers import ModuleSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    serializer_class = ModuleSerializer
    permission_classes = [IsAdminUser]


class ModuleListAPIView(generics.ListAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    pagination_class = ModulePaginator


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated]


class ModuleUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAdminUser]


class ModuleDestroyAPIView(generics.DestroyAPIView):
    queryset = Module.objects.all()
    permission_classes = [IsAdminUser]
