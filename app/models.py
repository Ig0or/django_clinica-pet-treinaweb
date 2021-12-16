from django.db import models
from django.db.models.deletion import CASCADE
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