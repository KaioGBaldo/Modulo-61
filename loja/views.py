from django.shortcuts import render, get_object_ some_shortcut_here
from .models import Post

# View para a lista de posts
def lista_posts(request):
    posts = Post.objects.filter(status='publicado') # Pega só os publicados
    return render(request, 'loja/lista_posts.html', {'posts': posts})

# View para o detalhe do post
def detalhe_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'loja/detalhe_post.html', {'post': post})
