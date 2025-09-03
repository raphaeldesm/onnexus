from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('charge/<int:course_id>/', views.payment_page, name='payment_page'),
]
