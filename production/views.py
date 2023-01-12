from rest_framework import generics
from django.http import JsonResponse
from rest_framework.response import Response

from production.models import AluminiumProfile, LightModule, Driver, Cover, MountingSystem
from production.serializers import ProfileSerializer, LightModuleSerializer, DriverSerializer, CoverSerializer, \
    MountingSystemSerializer


class AluminiumProfileAPI(generics.ListAPIView):
    queryset = AluminiumProfile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'Добавлено': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Invalid'})
        try:
            instance = AluminiumProfile.objects.get(pk=pk)
        except:
            return Response({'error': 'Not exists'})

        serializer = ProfileSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'update': serializer.data})


class LightModuleAPI(generics.ListAPIView):
    queryset = LightModule.objects.all()
    serializer_class = LightModuleSerializer

    def post(self, request):
        serializer = LightModuleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'Добавлено': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Invalid'})
        try:
            instance = LightModule.objects.get(pk=pk)
        except:
            return Response({'error': 'Not exists'})

        serializer = LightModuleSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'update': serializer.data})


class DriversAPI(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'Добавлено': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Invalid'})
        try:
            instance = Driver.objects.get(pk=pk)
        except:
            return Response({'error': 'Not exists'})

        serializer = DriverSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'update': serializer.data})


class CoversAPI(generics.ListAPIView):
    queryset = Cover.objects.all()
    serializer_class = CoverSerializer

    def post(self, request):
        serializer = CoverSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'Добавлено': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Invalid'})
        try:
            instance = Cover.objects.get(pk=pk)
        except:
            return Response({'error': 'Not exists'})

        serializer = CoverSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'update': serializer.data})


class MountingSystemAPI(generics.ListAPIView):
    queryset = MountingSystem.objects.all()
    serializer_class = MountingSystemSerializer

    def post(self, request):
        serializer = MountingSystemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'Добавлено': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Invalid'})
        try:
            instance = MountingSystem.objects.get(pk=pk)
        except:
            return Response({'error': 'Not exists'})

        serializer = MountingSystemSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'update': serializer.data})


def index(request):
    return HttpResponse('start app')
