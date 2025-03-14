from django.urls import path
from website import views
from website.views import *

urlpatterns = [
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/', views.clientes_view, name='clientes'),
    path('clientes/lista/', views.lista_clientes_view, name='lista_clientes'),
    path('cliente/editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('cliente/excluir/<int:cliente_id>/', views.excluir_cliente, name='excluir_cliente'),

    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/pagina/', views.produtos_view, name='produtos'),
    path('cadastrar-produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produto/editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('produto/excluir/<int:produto_id>/', views.excluir_produto, name='excluir_produto'),




    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedido/editar/<int:pedido_id>/', views.editar_pedido, name='editar_pedido'),
    path('pedido/excluir/<int:pedido_id>/', views.excluir_pedido, name='excluir_pedido'),


    path('pedido/cadastrar/<int:produto_id>/', views.cadastrar_pedido, name='cadastrar_pedido'),
    # Nova URL para cadastrar pedido

    path('', views.index, name='index'),
]
