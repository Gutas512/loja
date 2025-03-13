from django.urls import path
from website import views
from website.views import *

urlpatterns = [
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/', views.clientes_view, name='clientes'),
    path('clientes/lista/', views.lista_clientes_view, name='lista_clientes'),


    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/pagina/', views.produtos_view, name='produtos'),
    path('cadastrar-produto/', views.cadastrar_produto, name='cadastrar_produto'),

    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),

    path('pedido/cadastrar/<int:produto_id>/', views.cadastrar_pedido, name='cadastrar_pedido'),
    # Nova URL para cadastrar pedido

    path('', views.index, name='index'),
]
