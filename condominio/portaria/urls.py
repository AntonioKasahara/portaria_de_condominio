from django.urls import path
from . import views

app_name = 'portaria'

urlpatterns = [
    path('', views.pagina_inicial, name='index'),
    path('moradores/cadastro/', views.cadastro_morador, name='cadastro_morador'),
    path('entregas/cadastro/', views.cadastro_entregas, name='cadastro_entregas'),
    path('entradas/verificacao/', views.verificacao_entradas, name='verificacao_entradas'),
    path('funcionarios/cadastro/', views.cadastro_funcionarios, name='cadastro_funcionarios'),
    path('ocorrencias/registro/', views.registro_ocorrencias, name='registro_ocorrencias'),
]