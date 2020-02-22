from rest_framework import serializers
from .models import Aliment, Food


class AlimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aliment
        fields = ["id", "name", "price", "vitamin", "glucose", "protein", "lipid", "minerals"]


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ["id", "name", "price", "aliment"]


