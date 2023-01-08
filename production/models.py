from django.db import models


class AluminiumProfile(models.Model):
    profile = models.CharField(max_length=30)
    value = models.FloatField()
    date_update = models.DateTimeField(auto_now_add=True)
    date_delete = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profile


class LightModule(models.Model):
    module = models.CharField(max_length=30)
    value = models.FloatField()
    date_update = models.DateTimeField(auto_now_add=True)
    date_delete = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.module


class Driver(models.Model):
    drivers = models.CharField(max_length=30)
    value = models.IntegerField()
    date_update = models.DateTimeField(auto_now_add=True)
    date_delete = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.drivers


class Cover(models.Model):
    cover = models.CharField(max_length=30)
    value = models.IntegerField()
    date_update = models.DateTimeField(auto_now_add=True)
    date_delete = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cover


class MountingSystem(models.Model):
    mounting_system = models.CharField(max_length=30)
    value = models.IntegerField()
    date_update = models.DateTimeField(auto_now_add=True)
    date_delete = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mounting_system

