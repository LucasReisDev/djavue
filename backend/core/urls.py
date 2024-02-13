
from django.urls import path, include
from rest_framework import routers
from api.views import ClienteViewSet, ProdutoViewSet, GrupoProdutoViewSet, VendaViewSet, VendedorViewSet, ItemVendaViewSet, DashboardViewSet, GerarRelatorioPDF,GerarRelatorioExcel
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'grupos', GrupoProdutoViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'vendedores', VendedorViewSet)
router.register(r'itens', ItemVendaViewSet)
router.register(r'dashboard', DashboardViewSet, basename='dashboard')


urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', DashboardViewSet.as_view({'get': 'dashboard'}), name='dashboard'),
    path('gerar_relatorio_pdf/', GerarRelatorioPDF.as_view(), name='gerar_relatorio_pdf'),
    path('gerar_relatorio_excel/', GerarRelatorioExcel.as_view(), name='gerar_relatorio_excel'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
