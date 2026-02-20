from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.lista_posts, name='lista_posts'),
    path('blog/<slug:slug>/', views.detalhe_post, name='detalhe_post'),
]
