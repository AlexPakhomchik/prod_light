import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.pagination import PageNumberPagination
from production.models import AluminiumProfile, LightModule, Driver, Cover, MountingSystem, Lamp, History_log
from production.serializers import ProfileSerializer, LightModuleSerializer, DriverSerializer, CoverSerializer, \
    MountingSystemSerializer, LampSerializer, HistoryLogSerializer
from datetime import datetime, timedelta


class HistoryLogApi(viewsets.ModelViewSet):
    now = datetime.utcnow()
    seven_days_ago = now - timedelta(days=7)
    queryset = History_log.objects.filter(date_update__gte=seven_days_ago)
    serializer_class = HistoryLogSerializer

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass



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


class LampAPI(viewsets.ModelViewSet):
    queryset = Lamp.objects.all()
    serializer_class = LampSerializer
    pagination_class = PageNumberPagination


@csrf_exempt
def delete_materials_lamp(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        materials_lamp = json.loads(data)
        dict_bd = {'profile': AluminiumProfile, 'module': LightModule,
                   'driver': Driver, 'cover': Cover,
                   'mounting_system': MountingSystem}
        counter_keys = 0
        for material_type, material_data in materials_lamp.items():
            for material, count_dict in material_data.items():
                count = material_data['value']
                obj = dict_bd[material].objects.get(**{material: count_dict})
                if obj.value - count >= 0:
                    obj.value -= count
                    counter_keys += 1
                    obj.save()
                    break
                else:
                    return HttpResponse(status=400)
        return HttpResponse(status=204)
    else:
        return HttpResponseBadRequest()


def index(request):
    return HttpResponse('start app')
