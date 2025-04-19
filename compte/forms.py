from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    password = forms.CharField(label="Mot de Passe",widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))
