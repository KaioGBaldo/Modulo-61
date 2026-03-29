from django.urls import path
from . import views

app_name = 'loja'

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('post/<int:pk>/', views.detalhe_post, name='detalhe_post'),
]
