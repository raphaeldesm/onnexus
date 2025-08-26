from django import forms

class LoginForms(forms.Form):
    email = forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
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
    phone_number = forms.CharField(
        required=True,
        max_length=11,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'})
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
