from rest_framework import serializers
from warranty.models import Server


class ServerSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    make = serializers.CharField(max_length=50)
    model = serializers.CharField(max_length=50)
    serial = serializers.CharField(max_length=50)

    def create(self, validate_data):
        return Server.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.serial = validated_data.get('serial',instance.serial)
        instance.make = validated_data.get('make',instance.make)
        instance.model = validated_data.get('model',instance.model)
        instance.save()
        return instance