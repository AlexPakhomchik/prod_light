"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from production.views import index, AluminiumProfileAPI, LightModuleAPI, DriversAPI, CoversAPI, MountingSystemAPI

router = routers.SimpleRouter()
router.register(r'profile', AluminiumProfileAPI)
router.register(r'module', LightModuleAPI)
router.register(r'driver', DriversAPI)
router.register(r'cover', CoversAPI)
router.register(r'mounting_system', MountingSystemAPI)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('start/', index),
    path('api/', include(router.urls)),
]
