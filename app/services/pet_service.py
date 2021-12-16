from ..models import Pet

def cadastrar_pet(pet):
    Pet.objects.create(nome=pet.nome, data_nascimento=pet.data_nascimento, categoria=pet.categoria, cor=pet.cor, dono=pet.dono)


def listar_pet_id(id):
    return Pet.objects.get(id=id)
