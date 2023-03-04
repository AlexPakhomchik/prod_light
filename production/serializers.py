from rest_framework import serializers

from production.models import AluminiumProfile, LightModule, Driver, Cover, MountingSystem, Lamp, History_log


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AluminiumProfile
        fields = ('id', 'profile', 'value')


class LightModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightModule
        fields = ('id', 'module', 'value')


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'driver', 'value')


class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cover
        fields = ('id', 'cover', 'value')



class MountingSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountingSystem
        fields = ('id', 'mounting_system', 'value')


class LampSerializer(serializers.ModelSerializer):
    use_profile = serializers.StringRelatedField()
    use_module = serializers.StringRelatedField()
    use_driver = serializers.StringRelatedField()
    use_cover = serializers.StringRelatedField()
    use_mounting_system = serializers.StringRelatedField()

    class Meta:
        model = Lamp
        fields = ('id', 'name_lamp', 'use_profile', 'value_profile', 'use_module', 'value_module', 'use_driver',
                  'value_driver', 'use_cover', 'value_cover', 'use_mounting_system', 'value_mounting_system')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['use_profile'] = instance.use_profile.profile
        data['use_module'] = instance.use_module.module
        data['use_driver'] = instance.use_driver.driver
        data['use_cover'] = instance.use_cover.cover
        data['use_mounting_system'] = instance.use_mounting_system.mounting_system
        return data


class HistoryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = History_log
        fields = ('user', 'action', 'material', 'value', 'date_update')

