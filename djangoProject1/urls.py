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
from User.views import check_telegram_id, check_functionality, get_username_by_telegram_id
from production.views import index, AluminiumProfileAPI, LightModuleAPI, DriversAPI, CoversAPI, MountingSystemAPI, \
    LampAPI, delete_materials_lamp, HistoryLogApi

router = routers.SimpleRouter()
router.register(r'profile', AluminiumProfileAPI)
router.register(r'module', LightModuleAPI)
router.register(r'driver', DriversAPI)
router.register(r'cover', CoversAPI)
router.register(r'mounting_system', MountingSystemAPI)
router.register(r'lamp', LampAPI)
router.register(r'history_log', HistoryLogApi)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('start/', index),
    path('api/', include(router.urls)),
    path('check_telegram_id/', check_telegram_id),
    path('delete_materials_lamp/', delete_materials_lamp),
    path('check_functionality/', check_functionality),
    path('get_username_by_telegram_id/<int:telegram_id>/', get_username_by_telegram_id),
]
