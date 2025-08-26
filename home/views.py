from django.shortcuts import render, redirect
from .models import Post
from courses.models import Course

def home(request):
    posts = Post.objects.all()
    courses = Course.objects.all()

    return render(request, 'home/home-base.html', {'posts': posts, 'courses': courses})
