from django.shortcuts import render

def lista_produtos(request):
    produtos = [
        {'nome': 'Notebook', 'preco': 3500, 'disponivel': True},
        {'nome': 'Mouse', 'preco': 150, 'disponivel': True},
        {'nome': 'Teclado', 'preco': 250, 'disponivel': False},
    ]

    contexto = {
        'produtos': produtos,
        'titulo': 'Lista de Produtos'
    }

    return render(request, 'lista_produtos.html', contexto)
