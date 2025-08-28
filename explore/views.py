from django.shortcuts import render
from home.models import Post

# Create your views here.
def explore(request):
    posts = Post.objects.all()

    return render(request, 'explore/explore.html', {'posts': posts})