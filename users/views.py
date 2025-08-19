from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request, 'users/register.html')

def password_reset(request):
    return render(request, 'users/password_reset.html')

def password_recovery_code(request):
    return render(request, 'users/password_recovery_code.html')
