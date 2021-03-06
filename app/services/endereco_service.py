from ..models import EnderecoCliente

def cadastrar_endereco(endereco):
    return EnderecoCliente.objects.create(rua=endereco.rua, numero=endereco.numero, complemento=endereco.complemento, cidade=endereco.cidade, estado=endereco.estado)

def listar_endereco_id(id):
    return EnderecoCliente.objects.get(id=id)

def editar_endereco(endereco_antigo, endereco_novo):
    endereco_antigo.rua = endereco_novo.rua
    endereco_antigo.numero = endereco_novo.numero
    endereco_antigo.complemento = endereco_novo.complemento
    endereco_antigo.cidade = endereco_novo.cidade
    endereco_antigo.estado = endereco_novo.estado
    endereco_antigo.save(force_update=True)
    return endereco_antigo

def remover_endereco(endereco):
    endereco.delete()