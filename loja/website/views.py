from django.shortcuts import render, redirect
from loja.forms import ClienteForm, ProdutoForm, PedidoForm
from loja.models import Cliente, Produto, Pedido

# View para criar Cliente
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  # você pode ajustar esse destino
    else:
        form = ClienteForm()
    return render(request, 'cadastrar_cliente.html', {'form': form})

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o produto no banco de dados
            return redirect('lista_produtos')  # Redireciona para a lista de produtos
    else:
        form = ProdutoForm()  # Exibe o formulário vazio

    return render(request, 'cadastrar_produto.html', {'form': form})

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


def lista_clientes_view(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def clientes_view(request):
    return render(request, 'clientes.html')

def produtos_view(request):
    return render(request, 'produtos.html')

def pedidos_view(request):
    return render(request, 'pedidos.html')

def lista_pedidos(request):
    pedidos = Pedido.objects.select_related('cli_id', 'pro_id').all()
    return render(request, 'pedidos.html', {'pedidos': pedidos})

def lista_produtos(request):
    produtos = Produto.objects.all()  # Pega todos os produtos cadastrados
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def lista_clientes(request):
    clientes = Cliente.objects.all()  # Pega todos os clientes
    return render(request, 'lista_clientes.html', {'clientes': clientes})


def cadastrar_pedido(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        cliente = Cliente.objects.get(id=cliente_id)
        ped_data = request.POST.get('ped_data')

        pedido = Pedido.objects.create(cli_id=cliente, pro_id=produto, ped_data=ped_data)
        return redirect('lista_pedidos')  # Redireciona para a lista de pedidos

    return render(request, 'cadastrar_pedido.html', {'produto': produto, 'clientes': clientes})

# Editar cliente
def editar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'editar_cliente.html', {'form': form})

# Excluir cliente
def excluir_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'excluir_cliente.html', {'cliente': cliente})

def editar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'editar_produto.html', {'form': form})

def excluir_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'excluir_produto.html', {'produto': produto})

def editar_pedido(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'editar_pedido.html', {'form': form})

def excluir_pedido(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('lista_pedidos')
    return render(request, 'excluir_pedido.html', {'pedido': pedido})


def index(request):
    return render(request, 'index.html')