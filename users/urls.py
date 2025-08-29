from django.urls import path
from .views import register, login, logout_view, password_reset, password_recovery_code


app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout', logout_view, name='logout_view'),
    path('password_reset/', password_reset, name='password_reset'),
    path('password_recovery_code/', password_recovery_code, name='password_recovery_code'),
]
