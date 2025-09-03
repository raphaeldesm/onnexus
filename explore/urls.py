from django.urls import path
from . import views

app_name = 'explore'

urlpatterns = [
    path('', views.explore, name='explore'),
    path('hire/', views.hire, name='hire'),
]
