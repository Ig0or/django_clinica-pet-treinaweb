from ..models import EnderecoCliente

def cadastrar_endereco(endereco):
    return EnderecoCliente.objects.create(rua=endereco.rua, numero=endereco.rua, complemento=endereco.complemento, cidade=endereco.cidade, estado=endereco.estado)