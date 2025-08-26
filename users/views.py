from django.shortcuts import render, redirect

from users.forms import LoginForms, RegisterForms

from django.contrib.auth.models import User

from django.contrib import auth, messages

# Create your views here.
def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            email=form["email"].value()
            password=form["password"].value()

            user = auth.authenticate(
                request, 
                email=email,
                password=password
            )
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('home')
            else:
                messages.error(request, 'Email ou senha incorretos')
                return redirect('home')
            

    return render(request, 'users/login.html', {'form': form})

def register(request):
    form = RegisterForms()

    if request.method == 'POST':
        form = RegisterForms(request.POST)

        if form.is_valid():
            username=form["username"].value()
            phone_number=form["phone_number"].value()
            email=form["email"].value()
            password=form["password"].value()

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já existe')
                return redirect('register')
            
            user = User.objects.create_user(username=username, phone_number=phone_number, email=email, password=password)
            user.save()
            messages.success(request, 'Usuário cadastrado com sucesso')
            return redirect('login')


    return render(request, 'users/register.html', {'form': form})


def password_reset(request):
    return render(request, 'users/password_reset.html')

def password_recovery_code(request):
    return render(request, 'users/password_recovery_code.html')
