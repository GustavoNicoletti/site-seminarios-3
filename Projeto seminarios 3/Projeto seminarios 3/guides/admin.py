from django.contrib import admin
from .models import GuiaRapido

@admin.register(GuiaRapido)
class GuiaRapidoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao')
    # Organiza os campos em grupos visualmente separados
    fieldsets = (
        ("Informações Básicas", {
            'fields': ('titulo', 'conteudo')
        }),
        ("Dicas e Estratégias", {
            'fields': ('dicas', 'acoes_rapidas'),
            'description': "Preencha com orientações práticas para o dia a dia."
        }),
    )