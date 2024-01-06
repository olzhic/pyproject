from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 255)
    description = serializers.CharField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Order(**validated_data)
    
    def update(self, instance: Order, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance