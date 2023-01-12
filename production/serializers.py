from rest_framework import serializers

from production.models import AluminiumProfile, LightModule, Driver, Cover, MountingSystem


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AluminiumProfile
        fields = ('profile', 'value')

    def create(self, validate_data):
        return AluminiumProfile.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.profile = validate_data.get('profile', instance.profile)
        instance.value = validate_data.get('value', instance.value)
        instance.date_update = validate_data.get('date_update', instance.date_update)
        instance.date_delete = validate_data.get('date_delete', instance.date_delete)
        instance.save()
        return instance


class LightModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightModule
        fields = ('module', 'value')

    def create(self, validate_data):
        return LightModule.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.module = validate_data.get('module', instance.module)
        instance.value = validate_data.get('value', instance.value)
        instance.date_update = validate_data.get('date_update', instance.date_update)
        instance.date_delete = validate_data.get('date_delete', instance.date_delete)
        instance.save()
        return instance


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('drivers', 'value')

    def create(self, validate_data):
        return Driver.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.drivers = validate_data.get('drivers', instance.drivers)
        instance.value = validate_data.get('value', instance.value)
        instance.date_update = validate_data.get('date_update', instance.date_update)
        instance.date_delete = validate_data.get('date_delete', instance.date_delete)
        instance.save()
        return instance


class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cover
        fields = ('cover', 'value')

    def create(self, validate_data):
        return Cover.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.cover = validate_data.get('cover', instance.cover)
        instance.value = validate_data.get('value', instance.value)
        instance.date_update = validate_data.get('date_update', instance.date_update)
        instance.date_delete = validate_data.get('date_delete', instance.date_delete)
        instance.save()
        return instance


class MountingSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountingSystem
        fields = ('mounting_system', 'value')

    def create(self, validate_data):
        return MountingSystem.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.mounting_system = validate_data.get('mounting_system', instance.mounting_system)
        instance.value = validate_data.get('value', instance.value)
        instance.date_update = validate_data.get('date_update', instance.date_update)
        instance.date_delete = validate_data.get('date_delete', instance.date_delete)
        instance.save()
        return instance
