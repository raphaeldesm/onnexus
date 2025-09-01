from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class LoginForms(forms.Form):
    email = forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'exemplo@email.com'
            }
        )
    )
    password = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha'
            }
        )
    )




class RegisterForms(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome Completo'
            }
        )
    )
    email = forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'})
    )
    password = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Crie uma senha'}))

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, label='Nome', widget=forms.TextInput(attrs={'placeholder': ''}))
    last_name = forms.CharField(max_length=30, required=False, label='Sobrenome', widget=forms.TextInput(attrs={'placeholder': ''}))

    class Meta:
        model = UserProfile
        fields = ['occupation', 'company', 'location', 'city', 'bio', 'profile_picture']
        widgets = {
            'occupation': forms.TextInput(attrs={'placeholder': ''}),
            'company': forms.TextInput(attrs={'placeholder': ''}),
            'location': forms.TextInput(attrs={'placeholder': ''}),
            'city': forms.TextInput(attrs={'placeholder': ''}),
            'bio': forms.Textarea(attrs={'placeholder': ''}),
            'profile_picture': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name

    def save(self, commit=True):
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        profile = super(ProfileForm, self).save(commit=False)
        profile.occupation = self.cleaned_data['occupation']
        profile.company = self.cleaned_data['company']
        profile.location = self.cleaned_data['location']
        profile.city = self.cleaned_data['city']
        profile.bio = self.cleaned_data['bio']

        if 'profile_picture' in self.files:
            profile.profile_picture = self.cleaned_data['profile_picture']
        
        if commit:
            user.save()
            profile.save()
            
        return profile

class SocialLinksForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['site_title', 'site_url', 'linkedin_url', 'tiktok_url', 'instagram_url', 'whatsapp_number', 'other_social_url']
        widgets = {
            'site_title': forms.TextInput(attrs={'placeholder': 'Título do site'}),
            'site_url': forms.URLInput(attrs={'placeholder': 'Inserir url'}),
            'linkedin_url': forms.URLInput(attrs={'placeholder': 'Inserir url'}),
            'tiktok_url': forms.URLInput(attrs={'placeholder': 'Inserir url'}),
            'instagram_url': forms.URLInput(attrs={'placeholder': 'Inserir url'}),
            'whatsapp_number': forms.TextInput(attrs={'placeholder': '(00) 000-000-000'}),
            'other_social_url': forms.URLInput(attrs={'placeholder': 'Inserir url do YouTube, Facebook ou Flickr'}),
        }

class AccountSettingsForm(forms.Form):
    username = forms.CharField(required=True, label='Nome de usuário', widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome de usuário'}))
    email = forms.EmailField(required=True, label='E-mail', widget=forms.EmailInput(attrs={'placeholder': 'Digite seu melhor e-mail'}))
    contact_number = forms.CharField(max_length=20, required=False, label='Contato', widget=forms.TextInput(attrs={'placeholder': '(00) 000-000-000'}))
    new_password = forms.CharField(required=False, label='Nova senha', widget=forms.PasswordInput(attrs={'placeholder': 'Criar nova senha', 'autocomplete': 'new-password'}))
    confirm_password = forms.CharField(required=False, label='Confirmar senha', widget=forms.PasswordInput(attrs={'placeholder': 'Repita sua senha', 'autocomplete': 'new-password'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AccountSettingsForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['username'].initial = self.user.username
            self.fields['email'].initial = self.user.email
            if hasattr(self.user, 'userprofile'):
                self.fields['contact_number'].initial = self.user.userprofile.whatsapp_number

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and new_password != confirm_password:
            self.add_error('confirm_password', "As senhas não coincidem.")
        return cleaned_data

    def save(self, commit=True):
        user = self.user
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        
        new_password = self.cleaned_data.get("new_password")
        if new_password:
            user.set_password(new_password)
        
        if commit:
            user.save()

        profile, created = UserProfile.objects.get_or_create(user=user)
        profile.whatsapp_number = self.cleaned_data['contact_number']
        if commit:
            profile.save()
        
        return user
