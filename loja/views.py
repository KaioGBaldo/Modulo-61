from django.shortcuts import render, get_object_or_404
from .models import Post

def lista_posts(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'lista_posts.html', {'posts': posts})

def detalhe_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detalhe_post.html', {'post': post})
