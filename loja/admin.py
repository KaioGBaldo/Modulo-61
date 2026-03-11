from django.contrib import admin
from .models import Produto, Estoque, Post

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'criado_em')
    search_fields = ('nome',)
    list_filter = ('criado_em',)

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'quantidade', 'local')
    search_fields = ('produto__nome',)
    list_filter = ('local',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'criado_em')
    prepopulated_fields = {'slug': ('titulo',)} # Facilita a criação do slug
    search_fields = ('titulo',)
