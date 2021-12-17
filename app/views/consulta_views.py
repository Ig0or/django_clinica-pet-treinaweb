from django.shortcuts import render, redirect
from ..forms import consulta_forms
from ..services import pet_service, consulta_service
from ..entidades import consulta


def cadastrar_consulta(request, id):
    if request.method == 'POST':
        form_consulta = consulta_forms.ConsultaPetForm(request.POST)
        pet = pet_service.listar_pet_id(id)
        if form_consulta.is_valid():
            motivo_consulta = form_consulta.cleaned_data['motivo_consulta']
            peso_atual = form_consulta.cleaned_data['peso_atual']
            medicamento_atual = form_consulta.cleaned_data['medicamento_atual']
            medicamentos_prescritos = form_consulta.cleaned_data['medicamentos_prescritos']
            exames_prescritos = form_consulta.cleaned_data['exames_prescritos']
            consulta_nova = consulta.ConsultaPet(pet=pet, motivo_consulta=motivo_consulta, peso_atual=peso_atual, medicamento_atual=medicamento_atual, medicamentos_prescritos=medicamentos_prescritos, exames_prescritos=exames_prescritos)
            consulta_service.cadastrar_consulta(consulta_nova)
            return redirect('listar_pet_id', pet.id)
    else:
        form_consulta = consulta_forms.ConsultaPetForm()
    return render(request, 'consultas/form_consulta.html', {'form_consulta': form_consulta})

