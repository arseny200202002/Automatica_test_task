from rest_framework import serializers

from .models import Shop, Visit

class ShopSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Shop
        fields = ('pk', 'name')

class ShopListSerializer(serializers.Serializer):
    shop = ShopSerializer(many=True)


class CreateVisitSerializer(serializers.Serializer):
    shop_id = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('pk', 'created_at')
    