from django.shortcuts import render
from home.models import Post

# Create your views here.
def explore(request):
    posts = Post.objects.all()

    return render(request, 'explore/explore.html', {'posts': posts})

from django.shortcuts import render, redirect

def hire(request):
    if request.method == 'POST':
        # Lógica para criar o projeto aqui
        # ...
        # Adiciona uma notificação na sessão
        request.session['new_notification'] = True
        return redirect('messaging:messages')
    return render(request, 'explore/hire.html')