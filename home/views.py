from django.shortcuts import render, redirect
from .models import Post
from courses.models import Course

def home(request):
    posts = Post.objects.filter().order_by('-id')[:4]
    courses = Course.objects.filter(title__icontains='Manipular Imagens com Photoshop')

    return render(request, 'home/home-base.html', {'posts': posts, 'courses': courses})
