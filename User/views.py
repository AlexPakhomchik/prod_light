from django.http import JsonResponse, Http404, HttpResponse

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from User.models import User


def check_telegram_id(request):
    username = request.GET.get('username')
    telegram_id = request.GET.get('telegram_id')
    user = User.objects.filter(username=username, telegram_id=telegram_id).exists()
    return JsonResponse({'result': user})


def check_functionality(request):
    telegram_id = request.GET.get('telegram_id')
    user = User.objects.filter(telegram_id=telegram_id).exists()
    if not user:
        return HttpResponse(status=403)
    else:
        return JsonResponse({'result': user})
