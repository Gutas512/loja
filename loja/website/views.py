from django.shortcuts import render, redirect
from loja.forms import ClienteForm, ProdutoForm, PedidoForm
from loja.models import Cliente, Produto, Pedido

# View para criar Cliente
def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_lista')  # Redireciona para a lista de clientes ou outra página
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form})

# View para criar Produto
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto_lista')
    else:
        form = ProdutoForm()
    return render(request, 'produto_form.html', {'form': form})

# View para criar Pedido
def criar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido_lista')
    else:
        form = PedidoForm()
    return render(request, 'pedido_form.html', {'form': form})


def index(request):
    return render(request, 'index.html')