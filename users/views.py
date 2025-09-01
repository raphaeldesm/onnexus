from django.shortcuts import render, redirect

from users.forms import LoginForms, RegisterForms, ProfileForm, SocialLinksForm, AccountSettingsForm

from django.contrib.auth.models import User

from django.contrib import auth, messages

from django.contrib.auth import logout

from django.views import View

from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def payment_methods(request):
    return render(request, 'users/payment_methods.html')


# Create your views here.
def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None

            if user is not None:
                authenticated_user = auth.authenticate(
                    request, 
                    username=user.username,
                    password=password
                )
                if authenticated_user is not None:
                    auth.login(request, authenticated_user)
                    messages.success(request, 'Login realizado com sucesso')
                    return redirect('/')
            
            messages.error(request, 'Email ou senha incorretos')
            return redirect('/users/login')

    return render(request, 'users/login.html', {'form': form})

def register(request):
    form = RegisterForms()

    if request.method == 'POST':
        form = RegisterForms(request.POST)

        if form.is_valid():
            username=form["username"].value()
            email=form["email"].value()
            password=form["password"].value()

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já existe')
                return redirect('/users/register')
            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Usuário cadastrado com sucesso')
            return redirect('/users/login')


    return render(request, 'users/register.html', {'form': form})


def password_reset(request):
    return render(request, 'users/password_reset.html')

def password_recovery_code(request):
    return render(request, 'users/password_recovery_code.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso')
    return redirect('/')

@login_required
def edit_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('users:edit_profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'users/edit_profile.html', {'form': form})

@login_required
def social_links(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = SocialLinksForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Links e redes sociais atualizados com sucesso!')
            return redirect('users:social_links')
    else:
        form = SocialLinksForm(instance=profile)

    return render(request, 'users/social_links.html', {'form': form})

@login_required
def account_settings(request):
    if request.method == 'POST':
        form = AccountSettingsForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações da conta atualizadas com sucesso!')
            return redirect('account_settings')
    else:
        form = AccountSettingsForm(user=request.user)

    return render(request, 'users/account_settings.html', {'form': form})

