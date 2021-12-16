from django import forms
from django.forms.widgets import DateInput
from ..models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['nome', 'data_nascimento', 'categoria', 'cor']
        widgets = {
            'data_nascimento': DateInput(
                attrs={'type': 'date'}
            ),
        }
