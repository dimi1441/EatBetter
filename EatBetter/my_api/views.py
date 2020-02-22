from django.shortcuts import render
from rest_framework import viewsets, permissions
from .permissions import IsOwner
from .models import Aliment, Food
from .serializers import AlimentSerializer, FoodSerializer


# Create your views here.
class ListAlimentsView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = AlimentSerializer
    queryset = Aliment.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(owner=self.request.user)
        return query_set

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ListFoodView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(owner=self.request.user)
        return query_set

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



