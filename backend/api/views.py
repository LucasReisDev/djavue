from rest_framework.viewsets import ViewSet
from rest_framework import viewsets
from .models import Cliente, Produto, GrupoProduto, Venda, Vendedor, ItemVenda
from .serializers import ClienteSerializer, ProdutoSerializer, GrupoProdutoSerializer, VendaSerializer, VendedorSerializer, ItemVendaSerializer,VendaDetalhadaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from core.utils import gerar_relatorio_pdf, gerar_relatorio_excel
from django.http import FileResponse
from django.db.models.signals import post_save
from django.dispatch import receiver

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class GrupoProdutoViewSet(viewsets.ModelViewSet):
    queryset = GrupoProduto.objects.all()
    serializer_class = GrupoProdutoSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return VendaDetalhadaSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = super().get_queryset()
        cliente_id = self.request.query_params.get('cliente_id')
        vendedor_id = self.request.query_params.get('vendedor_id')
        if cliente_id:
            queryset = queryset.filter(cliente_id=cliente_id)
        if vendedor_id:
            queryset = queryset.filter(vendedor_id=vendedor_id)
        return queryset

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

class ItemVendaViewSet(viewsets.ModelViewSet):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer


class GerarRelatorioExcel(APIView):
    def get(self, request):
        vendas = Venda.objects.all()  # Ou adicione filtros, se necessário
        dados = [{'data': venda.data, 'vendedor_nome': venda.vendedor.nome, 'cliente_nome': venda.cliente.nome, 'valor_total': venda.valor_total} for venda in vendas]
        relatorio_excel = gerar_relatorio_excel(dados)
        return FileResponse(open(relatorio_excel, 'rb'), as_attachment=True)
    
class GerarRelatorioPDF(APIView):
    def get(self, request):
        vendas = Venda.objects.all()  # Ou adicione filtros, se necessário
        dados = [{'data': venda.data, 'vendedor_nome': venda.vendedor.nome, 'cliente_nome': venda.cliente.nome, 'valor_total': venda.valor_total} for venda in vendas]
        relatorio_pdf = gerar_relatorio_pdf(dados)
        return FileResponse(open(relatorio_pdf, 'rb'), as_attachment=True)

"""
@api_view(['POST'])
def criar_produto(request):
    if request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            grupo_id = request.data.get('grupo')    
            grupo = GrupoProduto.objects.get(pk=grupo_id)
            produto = serializer.save(grupo=grupo)  # Associa o grupo ao produto
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
 
class DashboardViewSet(ViewSet):
    @action(detail=False, methods=['get'])
    def dashboard(self, request):
        data_inicio = request.GET.get('data_inicio')
        data_fim = request.GET.get('data_fim')
        vendedor_id = request.GET.get('vendedor_id')
        cliente_id = request.GET.get('cliente_id')
        
        # Filtre as vendas com base nos parâmetros de consulta
        vendas = Venda.objects.all()

        if data_inicio:
            vendas = vendas.filter(data__gte=data_inicio)
        if data_fim:
            vendas = vendas.filter(data__lte=data_fim)
        if vendedor_id:
            vendas = vendas.filter(vendedor_id=vendedor_id)
        if cliente_id:
            vendas = vendas.filter(cliente_id=cliente_id)
        
         # Serialize os dados das vendas
        serializer = VendaSerializer(vendas, many=True)
        vendas_json = serializer.data
        
        
        
        # Retorne os dados das vendas e os URLs dos relatórios em formato JSON
        return Response({
            'vendas': vendas_json
        })
    
