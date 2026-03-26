from django.db import models

class GuiaRapido(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título da Dica")
    conteudo = models.TextField(verbose_name="Contexto/Explicação")
    
    # Novos campos para dicas e ações
    dicas = models.TextField(verbose_name="Dicas Práticas", blank=True, null=True)
    acoes_rapidas = models.TextField(verbose_name="O que fazer (Ações Rápidas)", blank=True, null=True)
    
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Guia Rápido"
        verbose_name_plural = "Guias Rápidos"

    def __str__(self):
        return self.titulo