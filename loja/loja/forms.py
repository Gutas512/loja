from django import forms
from .models import Cliente, Produto, Pedido

# Formulário para Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cli_nome', 'cli_email', 'cli_telefone']

    # Adicionando algumas opções de personalização para os campos
    cli_nome = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cli_email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    cli_telefone = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control'}))

# Formulário para Produto
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['pro_nome', 'pro_descricao', 'pro_preco']

    pro_nome = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pro_descricao = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pro_preco = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

# Formulário para Pedido
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cli_id', 'pro_id', 'ped_data']

    cli_id = forms.ModelChoiceField(queryset=Cliente.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    pro_id = forms.ModelChoiceField(queryset=Produto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    ped_data = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
