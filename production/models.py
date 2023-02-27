from django.db import models
from django.contrib.auth.models import AbstractUser


class AluminiumProfile(models.Model):
    profile = models.CharField(max_length=30)
    value = models.FloatField(default=0)
    date_update = models.DateTimeField(auto_now_add=True)
    date_delete = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.profile} - {self.value} кг'


class LightModule(models.Model):
    module = models.CharField(max_length=30)
    value = models.FloatField(default=0)
    date_update = models.DateTimeField(auto_now_add=True)
    date_delete = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.module} - {self.value} шт'


class Driver(models.Model):
    driver = models.CharField(max_length=30)
    value = models.IntegerField(default=0)
    date_update = models.DateTimeField(auto_now_add=True)
    date_delete = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.driver} - {self.value} шт'


class Cover(models.Model):
    cover = models.CharField(max_length=30)
    value = models.IntegerField(default=0)
    date_update = models.DateTimeField(auto_now_add=True)
    date_delete = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cover} - {self.value} шт'


class MountingSystem(models.Model):
    mounting_system = models.CharField(max_length=30)
    value = models.IntegerField(default=0)
    date_update = models.DateTimeField(auto_now_add=True)
    date_delete = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.mounting_system} - {self.value} шт'


class Lamp(models.Model):
    name_lamp = models.CharField(max_length=70)
    use_profile = models.ForeignKey(AluminiumProfile,on_delete= models.CASCADE)
    value_profile = models.FloatField(default=0)
    use_module = models.ForeignKey(LightModule, on_delete=models.CASCADE)
    value_module = models.FloatField(default=0)
    use_driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    value_driver = models.IntegerField(default=0)
    use_cover = models.ForeignKey(Cover, on_delete=models.CASCADE)
    value_cover = models.IntegerField(default=0)
    use_mounting_system = models.ForeignKey(MountingSystem, on_delete=models.CASCADE)
    value_mounting_system = models.IntegerField(default=0)

    def __str__(self):
        return self.name_lamp

