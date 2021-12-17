from django.urls import path
from .views import cliente_views, pet_views, consulta_views

urlpatterns = [
    path('cadastrar_cliente', cliente_views.cadastrar_cliente, name='cadastrar_cliente'),
    path('listar_clientes', cliente_views.listar_clientes, name='listar_clientes'),
    path('lista_cliente/<int:id>', cliente_views.listar_clientes_id, name='listar_cliente_id'),
    path('editar_cliente/<int:id>', cliente_views.editar_cliente, name='editar_cliente'),
    path('remover_cliente/<int:id>', cliente_views.remover_cliente, name='remover_cliente'),
    path('cadastrar_pet/<int:id>', pet_views.cadastrar_pet, name='cadastrar_pet'),
    path('lista_pet/<int:id>', pet_views.listar_pet_id, name='listar_pet_id'),
    path('editar_pet/<int:id>', pet_views.editar_pet, name='editar_pet'),
    path('cadastrar_consulta/<int:id>', consulta_views.cadastrar_consulta, name='cadastrar_consulta'),
    path('lista_consulta/<int:id>', consulta_views.listar_consulta_id, name='lista_consulta_id')
]