from django import forms
from django.forms.widgets import DateInput
from ..models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'cpf', 'data_nascimento', 'profissao']
        widgets = {
            'data_nascimento': DateInput(
                attrs={'type': 'date'}
            ),
        }