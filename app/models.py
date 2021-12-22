from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from localflavor.br.br_states import STATE_CHOICES

class EnderecoCliente(models.Model):
    rua = models.CharField(max_length=50, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    complemento = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(max_length=2, choices=STATE_CHOICES, null=False, blank=False)

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    telefone = models.CharField(max_length=11, blank=False, null=False)
    endereco = models.ForeignKey(EnderecoCliente, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    profissao = models.CharField(max_length=25, null=False, blank=False)

class Pet(models.Model):
    CATEGORIA_CHOICES = (
        ('Dog', 'Cachorro'), 
        ('Cat', 'Gato'), 
        ('Bunny', 'Coelho')
    )
    COR_CHOICES = (
        ('Black', 'Preto'),
        ('White', 'Branco'),
        ('Gray', 'Cinz'),
        ('Brown', 'Marrom'),
    )
    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES, null=False, blank=False)
    cor =  models.CharField(max_length=10, choices=COR_CHOICES, null=False, blank=False)
    dono = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class ConsultaPet(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=False, blank=False)
    data = models.DateField(null=False, blank=False, auto_now_add=True)
    motivo_consulta = models.CharField(max_length=200, null=False, blank=False)
    peso_atual = models.FloatField(null=False, blank=False)
    medicamento_atual = models.TextField(null=False, blank=True)
    medicamentos_prescritos = models.TextField(null=False, blank=True)
    exames_prescritos = models.TextField(null=False, blank=True)


class Funcionario(AbstractUser):
    CARGOS_CHOICES = (
        ('1', 'Veterinário'),
        ('2', 'Financeiro'),
        ('3', 'Atendimento'),
    )

    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    cargo = models.CharField(max_length=10, choices=CARGOS_CHOICES, null=False, blank=False)
