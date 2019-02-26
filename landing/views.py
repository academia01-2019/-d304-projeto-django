from django.shortcuts import render

def mostrar_index(request):
    nome = 'Henrique'
    lista_compras = ['arroz', 'feijão', 'açai']
    return render(request, 'index.html', {'item' : nome, 'lista' : lista_compras})

def mostrar_sobre(request):
    return render(request, 'sobre.html')
