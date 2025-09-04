from django.shortcuts import render, redirect
from .models import Post
from courses.models import Course

def home(request):
    posts = Post.objects.all()
    courses = Course.objects.filter(title__icontains='Manipular Imagens com Photoshop')

    return render(request, 'home/home-base.html', {'posts': posts, 'courses': courses})

def privacy(request):
    return render(request, 'home/privacy.html')

def terms(request):
    return render(request, 'home/terms.html')
