from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_recovery_code/', views.password_recovery_code, name='password_recovery_code'),
]
