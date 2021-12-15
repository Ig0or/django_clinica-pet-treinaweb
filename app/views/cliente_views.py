from app.forms.cliente_forms import ClienteForm
from app.forms.endereco_forms import EnderecoClienteForm
from ..entidades import cliente, endereco
from ..services import cliente_service, endereco_service
from django.shortcuts import render


def cadastrar_cliente(request):
    if request.method == 'POST':
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoClienteForm(request.POST)
        if form_cliente.is_valid():
            nome = form_cliente.cleaned_data['nome']
            email = form_cliente.cleaned_data['email']
            telefone = form_cliente.cleaned_data['telefone']
            cpf = form_cliente.cleaned_data['cpf']
            data_nascimento = form_cliente.cleaned_data['data_nascimento']
            profissao = form_cliente.cleaned_data['profissao']
            if form_endereco.is_valid():
                rua = form_endereco.cleaned_data['rua']
                numero = form_endereco.cleaned_data['numero']
                complemento = form_endereco.cleaned_data['complemento']
                cidade = form_endereco.cleaned_data['cidade']
                estado = form_endereco.cleaned_data['estado']
                endereco_novo = endereco.Endereco(rua=rua, numero=numero, complemento=complemento, cidade=cidade, estado=estado)
                endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)
                cliente_novo = cliente.Cliente(nome=nome, email=email, telefone=telefone, cpf=cpf, data_nascimento=data_nascimento, profissao=profissao, endereco=endereco_bd)
                cliente_service.cadastrar_cliente(cliente_novo)
    else:
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoClienteForm(request.POST)
    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente, 'form_endereco': form_endereco})