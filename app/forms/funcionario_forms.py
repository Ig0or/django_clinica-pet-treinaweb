from django import forms
from django.forms.widgets import DateInput
from ..models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'
        widgets = {
            'data_nascimento': DateInput(
                attrs={'type': 'date'}
            ),
        }
