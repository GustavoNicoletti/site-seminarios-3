from django.db import models

class Estrategia(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")
    publico_alvo = models.CharField(max_length=200, blank=True, null=True, verbose_name="Público-alvo")
    objetivo = models.TextField(blank=True, null=True, verbose_name="Objetivo")
    passo_a_passo = models.TextField(blank=True, null=True, verbose_name="Passo a passo")
    materiais = models.TextField(blank=True, null=True, verbose_name="Materiais")
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Estratégia"
        verbose_name_plural = "Estratégias"

    def __str__(self):
        return self.titulo