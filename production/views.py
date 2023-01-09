from rest_framework import generics
from django.http import HttpResponse
from production.models import AluminiumProfile, LightModule, Driver, Cover, MountingSystem
from production.serializers import ProfileSerializer, LightModuleSerializer, DriverSerializer, CoverSerializer, \
    MountingSystemSerializer


class AluminiumProfileAPI(generics.ListAPIView):
    queryset = AluminiumProfile.objects.all()
    serializer_class = ProfileSerializer


class LightModuleAPI(generics.ListAPIView):
    queryset = LightModule.objects.all()
    serializer_class = LightModuleSerializer


class DriversAPI(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class CoversAPI(generics.ListAPIView):
    queryset = Cover.objects.all()
    serializer_class = CoverSerializer


class MountingSystemAPI(generics.ListAPIView):
    queryset = MountingSystem.objects.all()
    serializer_class = MountingSystemSerializer


def index(request):
    return HttpResponse('start app')
