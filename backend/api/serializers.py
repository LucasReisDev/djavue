from rest_framework import serializers
from .models import Cliente, Produto, GrupoProduto, Venda, Vendedor, ItemVenda

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class GrupoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoProduto
        fields = '__all__'


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'

class ItemVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVenda
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.CharField(source='cliente.nome', read_only=True)
    vendedor_nome = serializers.CharField(source='vendedor.nome', read_only=True)
    itens_venda = ItemVendaSerializer(many=True, read_only=True)

    class Meta:
        model = Venda
        fields = ['id', 'cliente', 'cliente_nome', 'vendedor', 'vendedor_nome', 'data', 'valor_total', 'itens_venda']

class VendaDetalhadaSerializer(serializers.ModelSerializer):
    itens_venda = ItemVendaSerializer(many=True, read_only=True)  # Assumindo que você já tem um serializer para o modelo ItemVenda

    class Meta:
        model = Venda
        fields = ['id', 'cliente', 'vendedor', 'data', 'valor_total', 'itens_venda']