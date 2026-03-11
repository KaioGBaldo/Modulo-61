from django.shortcuts import render, get_object_or_404
from .models import Post

def lista_posts(request):
    # Busca apenas posts publicados para exibir na lista
    posts = Post.objects.filter(status='publicado') 
    return render(request, 'loja/lista_posts.html', {'posts': posts})

def detalhe_post(request, slug):
    # Busca o post pelo slug ou retorna 404 se não existir
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'loja/detalhe_post.html', {'post': post})
