from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('biblioteca/', views.lista_estrategias, name='lista_estrategias'),
    path('biblioteca/nova/', views.cadastrar_estrategia, name='cadastrar_estrategia'),
    path('biblioteca/<int:pk>/', views.detalhe_estrategia, name='detalhe_estrategia'),
    path('biblioteca/<int:pk>/excluir/', views.excluir_estrategia, name='excluir_estrategia'),
]