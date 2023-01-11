from rest_framework import serializers

from production.models import AluminiumProfile, LightModule, Driver, Cover, MountingSystem


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AluminiumProfile
        fields = ('profile', 'value')

    def create(self, validate_data):
        return AluminiumProfile.objects.create(**validate_data)

class LightModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightModule
        fields = ('module', 'value')


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('driver', 'value')


class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cover
        fields = ('cover', 'value')


class MountingSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountingSystem
        fields = ('mounting_system', 'value')
