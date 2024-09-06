# house_price_analysis/serializers.py

from rest_framework import serializers
from .models import HousePrice, Region

class HousePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousePrice
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'