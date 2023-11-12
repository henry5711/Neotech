from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import PasswordChangeForm
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
    )

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingrese una dirección de correo electrónico válida.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        
        # Agregar el atributo placeholder a los campos
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['email'].widget.attrs['placeholder'] = 'Correo Electrónico'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
    
class UserProfileForm(forms.ModelForm):
    delete_profile_picture = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'name', 'last_name', 'document']
        
class ChangePasswordForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nueva contraseña'}),
        label='Nueva contraseña'
    )

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar nueva contraseña'}),
        label='Confirmar nueva contraseña'
    )

