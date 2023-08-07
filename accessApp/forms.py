from django import forms
from appHCI.models import UserZT

class UserForm(forms.ModelForm):
    passworddd=forms.CharField(max_length=60, label='Confirmar Contraseña')
    class Meta:
        model = UserZT
        fields = 'first_name','last_name','ci_user','fecha_nac','email','telefono','password'  # O especifica los campos que deseas incluir en el formulario
        labels={
            'username': 'Usuario',
            'password': 'Contraseña',

        }


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