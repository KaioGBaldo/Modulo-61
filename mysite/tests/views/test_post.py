import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b'Hello, World!!!!'
    
def test_post_detail(client):
    url = reverse('detail')
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b'Post details.'
    
def test_post_list(client):
    url = reverse('list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b'List Posts.'
    