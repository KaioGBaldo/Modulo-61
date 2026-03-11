from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    local = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}"

# --- NOVO MODELO PARA O BLOG ---
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    conteudo = models.TextField()
    status = models.CharField(
        max_length=10, 
        choices=[('rascunho', 'Rascunho'), ('publicado', 'Publicado')],
        default='rascunho'
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
