from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import make_password
from ..forms.funcionario_forms import FuncionarioForm
from ..entidades import funcionario
from ..services import funcionario_service

@user_passes_test(lambda u: u.cargo == '2')
def cadastrar_funcionario(request):
    if request.method == 'POST':
        form_funcionario = FuncionarioForm(request.POST)
        if form_funcionario.is_valid():
            nome = form_funcionario.cleaned_data['nome']
            data_nascimento = form_funcionario.cleaned_data['data_nascimento']
            cargo = form_funcionario.cleaned_data['cargo']
            username = form_funcionario.cleaned_data['username']
            password = make_password(form_funcionario.cleaned_data['password1'])
            funcionario_novo = funcionario.Funcionario(nome=nome, data_nascimento=data_nascimento, cargo=cargo, username=username, password=password)
            funcionario_service.cadastrar_funcionario(funcionario_novo)
            return redirect('listar_funcionarios')
    else:
        form_funcionario = FuncionarioForm()
    return render(request, 'funcionarios/form_funcionario.html', {'form_funcionario': form_funcionario})

@user_passes_test(lambda u: u.cargo == '2')
def listar_funcionarios(request):
    funcionarios = funcionario_service.listar_funcionarios()
    return render(request, 'funcionarios/lista_funcionarios.html', {'funcionarios': funcionarios})
