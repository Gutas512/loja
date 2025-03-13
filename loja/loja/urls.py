from django.urls import path
from website import views
from website.views import *

urlpatterns = [
    path('cliente/novo/', views.criar_cliente, name='criar_cliente'),

    path('produto/novo/', views.criar_produto, name='criar_produto'),

    path('pedido/novo/', views.criar_pedido, name='criar_pedido'),

    path('', views.index, name='index'),

]
