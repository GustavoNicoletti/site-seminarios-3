from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_guia, name='lista_guia'),
    path('novo/', views.cadastrar_guia, name='cadastrar_guia'),
    path('<int:pk>/', views.detalhe_guia, name='detalhe_guia'),
    path('<int:pk>/excluir/', views.excluir_guia, name='excluir_guia'), # Nova rota
]