from django.db import models


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

