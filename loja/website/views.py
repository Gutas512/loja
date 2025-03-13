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


def index(request):
    return render(request, 'index.html')