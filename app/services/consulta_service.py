from ..models import ConsultaPet
from ..services import pet_service

def cadastrar_consulta(consulta):
    consulta_bd = ConsultaPet.objects.create(pet=consulta.pet, motivo_consulta=consulta.motivo_consulta, peso_atual=consulta.peso_atual, medicamento_atual=consulta.medicamento_atual, medicamentos_prescritos=consulta.medicamentos_prescritos, exames_prescritos=consulta.exames_prescritos)
    consulta_bd.save()


def listar_consultas(id):
    return ConsultaPet.objects.filter(pet=id).all()


def listar_consultas_pets(id):
    # pets = pet_service.listar_pets(id)
    # consultas = ConsultaPet.objects.filter(pet=pets.id).all()
    return ConsultaPet.objects.filter(pet__dono=id).all().order_by('-data')


def listar_consulta(id):
    return ConsultaPet.objects.get(id=id)