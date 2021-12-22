from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput
from ..models import Funcionario

class FuncionarioForm(UserCreationForm):
    class Meta:
        model = Funcionario
        fields = UserCreationForm.Meta.fields + ('nome', 'data_nascimento', 'cargo')
        widgets = {
            'data_nascimento': DateInput(
                attrs={'type': 'date'}
            ),
        }
