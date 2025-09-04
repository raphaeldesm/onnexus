from django.shortcuts import render, redirect
from django.http import JsonResponse

def clear_notifications(request):
    if 'new_notification' in request.session:
        del request.session['new_notification']
    return JsonResponse({'status': 'ok'})

def notifications_view(request):
    if 'new_notification' in request.session:
        del request.session['new_notification']
    # Futuramente, você pode buscar notificações do banco de dados aqui
    return render(request, 'notifications/notifications.html')
