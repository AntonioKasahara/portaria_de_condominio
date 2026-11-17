from django.shortcuts import render

# Create your views here.

def pagina_inicial(request):
    return render(request, 'portaria/index.html')

def cadastro_morador(request):
    return render(request, 'portaria/cadastro_morador.html')

def cadastro_entregas(request):
    return render(request, 'portaria/cadastro_entregas.html')

def verificacao_entradas(request):
    return render(request, 'portaria/verificacao_entradas.html')

def cadastro_funcionarios(request):
    return render(request, 'portaria/cadastro_funcionarios.html')

def registro_ocorrencias(request):
    return render(request, 'portaria/registro_ocorrencias.html')