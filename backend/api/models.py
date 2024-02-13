from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class GrupoProduto(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):    
    nome = models.CharField(max_length=100)
    grupo = models.ForeignKey(GrupoProduto, on_delete=models.CASCADE)
    preço = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)   

    def calcular_valor_total(self):
        itens_venda = ItemVenda.objects.filter(venda=self)
        total = sum(item.valor_total for item in itens_venda)
        self.valor_total = total
        self.save()

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)  

    def save(self, *args, **kwargs):
        # Atualiza o campo valor_total com base no preço do produto e na quantidade
        self.valor_total = self.produto.preço * self.quantidade
        super().save(*args, **kwargs)
        # Atualiza o valor_total da venda associada
        self.venda.calcular_valor_total()