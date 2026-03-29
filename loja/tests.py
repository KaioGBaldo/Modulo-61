import pytest
import factory
from django.contrib.auth.models import User
from loja.models import Post

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: f'user_{n}')

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
    title = 'Meu Post de Exemplo'
    content = 'Conteúdo do post para o teste EBAC.'
    author = factory.SubFactory(UserFactory)

@pytest.mark.django_db
def test_create_post():
    post = PostFactory()
    assert Post.objects.count() == 1
    assert post.title == 'Meu Post de Exemplo'
