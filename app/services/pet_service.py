from ..models import Pet

def cadastrar_pet(pet):
    Pet.objects.create(nome=pet.nome, data_nascimento=pet.data_nascimento, categoria=pet.categoria, cor=pet.cor, dono=pet.dono)


def listar_pet_id(id):
    return Pet.objects.get(id=id)


def listar_pets(id):
    return Pet.objects.filter(dono=id).all()


def editar_pet(pet_antigo, pet_novo):
    pet_antigo.nome = pet_novo.nome
    pet_antigo.data_nascimento = pet_novo.data_nascimento
    pet_antigo.categoria = pet_novo.categoria
    pet_antigo.cor = pet_novo.cor
    pet_antigo.dono = pet_novo.dono
    pet_antigo.save(force_update=True)
    return pet_antigo