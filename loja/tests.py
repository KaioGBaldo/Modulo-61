import pytest
import factory
from loja.models import Product

# Cria uma fábrica de produtos para os testes
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = 'Produto Padrão'
    description = 'Descrição do produto de teste'
    price = 50.00
    active = True

@pytest.mark.django_db
def test_create_product():
    # Cria um produto real no banco de dados de teste
    product = ProductFactory(title="Teclado Mecânico")
    
    assert product.title == "Teclado Mecânico"
    assert Product.objects.count() == 1
