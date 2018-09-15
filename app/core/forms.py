from django import forms

from . import models

class RegistrationUserForm(forms.ModelForm):
  
  class Meta:
    model = models.UUIDUser
    fields = ('username', 'email', 'password')
    labels = {
    	'username': 'Nome de Usuário',
    	'email': 'E-mail',
    	'password': 'Senha',
    }
    widgets = {
      'password': forms.PasswordInput()
    }