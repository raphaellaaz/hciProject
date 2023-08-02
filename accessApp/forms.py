from django import forms
from appHCI.models import UserZT

class UserForm(forms.ModelForm):
    class Meta:
        model = UserZT
        fields = '__all__'  # O especifica los campos que deseas incluir en el formulario

    