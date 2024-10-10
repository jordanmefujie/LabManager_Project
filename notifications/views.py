from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Notification
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def send_notification(user, message):
    notification = Notification.objects.create(user=user, message=message)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{user.id}",
        {
            "type": "send_notification",
            "message": message,
        }
    )

def notifications(request):
    return render(request, 'notifications/notifications.html')

@login_required
def get_notifications(request):
    notifications = Notification.objects.filter(user=request.user, read=False).order_by('-created_at')
    notification_data = [{"id": n.id, "message": n.message, "created_at": n.created_at.strftime("%Y-%m-%d %H:%M:%S")} for n in notifications]
    return JsonResponse(notification_data, safe=False)

@login_required
def mark_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.read = True
    notification.save()
    return JsonResponse({"success": True})
