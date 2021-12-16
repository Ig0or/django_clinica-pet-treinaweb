from django.shortcuts import render, redirect
from ..entidades.pet import Pet
from ..forms.pet_forms import PetForm
from ..services import cliente_service, pet_service

def cadastrar_pet(request, id):
    if request.method == 'POST':
        form_pet = PetForm(request.POST)
        if form_pet.is_valid():
            nome = form_pet.cleaned_data['nome']
            data_nascimento = form_pet.cleaned_data['data_nascimento']
            categoria = form_pet.cleaned_data['categoria']
            cor = form_pet.cleaned_data['cor']
            dono = cliente_service.listar_cliente_id(id)
            pet_novo = Pet(nome=nome, data_nascimento=data_nascimento, categoria=categoria, cor=cor, dono=dono)
            pet_service.cadastrar_pet(pet_novo)
    else:
        form_pet = PetForm()
    return render(request, 'pets/form_pet.html', {'form_pet': form_pet})


def listar_pet(request, id):
    pet = pet_service.listar_pet_id(id)
    return render(request, 'pets/lista_pet.html', {'pet': pet})