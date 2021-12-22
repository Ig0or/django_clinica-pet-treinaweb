from ..models import Funcionario

def cadastrar_funcionario(funcionario):
    Funcionario.objects.create(nome=funcionario.nome, data_nascimento=funcionario.data_nascimento, cargo=funcionario.cargo, username=funcionario.username, password=funcionario.password)


def listar_funcionarios():
    return Funcionario.objects.all()

