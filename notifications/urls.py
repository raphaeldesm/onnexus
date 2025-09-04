from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.notifications_view, name='list'),
    path('clear/', views.clear_notifications, name='clear'),
]
