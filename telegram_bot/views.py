from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Reminder


@require_POST
@csrf_exempt
def send_reminder(request):
    reminder = Reminder.objects.get(id=request.POST.get('id'))
    reminder.send_reminder()
    return JsonResponse({'status': 'ok'})
