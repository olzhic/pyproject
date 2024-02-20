from rest_framework import serializers
from .models import Contacts

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 255)
    number = serializers.CharField(max_length = 255)

    def create(self, validated_data):
        return Contacts(**validated_data)
    
    def update(self, instance: Contacts, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.number = validated_data.get('number', instance.number)
        instance.save()
        return instance