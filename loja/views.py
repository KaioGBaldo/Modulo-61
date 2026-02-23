from django.shortcuts import render, get_object_or_404
from .models import Post

def lista_posts(request):
    # Requisito: Dados enviados pela view
    posts = Post.objects.filter(status='publicado') 
    return render(request, 'loja/lista_posts.html', {'posts': posts})

def detalhe_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'loja/detalhe_post.html', {'post': post})
