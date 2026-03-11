from django.shortcuts import render, get_object_or_404
from .models import Post  # Agora o Post existirá

def lista_posts(request):
    # Filtra apenas os posts com status 'publicado'
    posts = Post.objects.filter(status='publicado') 
    return render(request, 'loja/lista_posts.html', {'posts': posts})

def detalhe_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'loja/detalhe_post.html', {'post': post})
