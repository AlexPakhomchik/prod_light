from django.shortcuts import HttpResponse

from production.models import AluminiumProfile, LightModule, Driver, Cover, MountingSystem


def index(request):
    return HttpResponse('start app')


def get_profile(request, prof):
    material = AluminiumProfile.objects.get(profile=prof)
    return HttpResponse(material)


def get_module(request, mod):
    material = LightModule.objects.get(module=mod)
    return HttpResponse(material)


def get_driver(request, drive):
    material = Driver.objects.get(drivers=drive)
    return HttpResponse(material)


def get_cover(request, cov):
    material = Cover.objects.get(cover=cov)
    return HttpResponse(material)


def get_mounting_system(request, moun):
    material = MountingSystem.objects.get(mounting_system=moun)
    return HttpResponse(material)