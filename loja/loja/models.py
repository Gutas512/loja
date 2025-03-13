from django.db import models

from django.db import models

# Modelo Cliente
class Cliente(models.Model):
    cli_nome = models.CharField(max_length=50)
    cli_email = models.EmailField(max_length=50)
    cli_telefone = models.CharField(max_length=14)

    def __str__(self):
        return self.cli_nome

# Modelo Produto
class Produto(models.Model):
    pro_nome = models.CharField(max_length=50)
    pro_descricao = models.CharField(max_length=50)
    pro_preco = models.FloatField()

    def __str__(self):
        return self.pro_nome

# Modelo Pedido
class Pedido(models.Model):
    cli_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pro_id = models.ForeignKey(Produto, on_delete=models.CASCADE)
    ped_data = models.DateField()

    def __str__(self):
        return f'Pedido {self.id} - {self.cli_id.cli_nome} - {self.ped_data}'

