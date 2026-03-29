import pytest
import factory
from loja.models import Product

# Fábrica para criar objetos de teste sem repetir código
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = 'Produto Teste'
    description = 'Uma descrição qualquer'
    price = 10.00
    active = True

@pytest.mark.django_db
def test_create_product():
    # Cria uma instância no banco de teste usando a factory
    product = ProductFactory(title="Camiseta EBAC")
    assert product.title == "Camiseta EBAC"
    assert Product.objects.count() == 1
