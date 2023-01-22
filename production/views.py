from rest_framework import generics, viewsets
from django.http import JsonResponse
from rest_framework.response import Response

from production.models import AluminiumProfile, LightModule, Driver, Cover, MountingSystem
from production.serializers import ProfileSerializer, LightModuleSerializer, DriverSerializer, CoverSerializer, \
    MountingSystemSerializer


class AluminiumProfileAPI(viewsets.ModelViewSet):
    queryset = AluminiumProfile.objects.all()
    serializer_class = ProfileSerializer


class LightModuleAPI(viewsets.ModelViewSet):
    queryset = LightModule.objects.all()
    serializer_class = LightModuleSerializer


class DriversAPI(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class CoversAPI(viewsets.ModelViewSet):
    queryset = Cover.objects.all()
    serializer_class = CoverSerializer


class MountingSystemAPI(viewsets.ModelViewSet):
    queryset = MountingSystem.objects.all()
    serializer_class = MountingSystemSerializer


def index(request):
    return HttpResponse('start app')
