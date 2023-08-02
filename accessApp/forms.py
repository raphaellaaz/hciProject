from django import forms
from appHCI.models import UserZT

class UserForm(forms.ModelForm):
    class Meta:
        model = UserZT
        fields = '__all__'  # O especifica los campos que deseas incluir en el formulario


class loginFormulario(forms.Form): ##Formulario de Incio de Sesion

    username = forms.CharField(max_length=60, label='Usuario')
    password = forms.CharField(max_length=60, label='Contraseña')
    
    class Meta:

        widgets={
            'username': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Username'
            }),
            'password': forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'Contraseña'
            }),
        }
        labels={
            'Username': 'Usuario',
            'Password': 'Contraseña',
        }