from django.contrib import admin
from .models import Aluno, VideoComplementar

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ra', 'turma')
    search_fields = ('nome', 'ra')

@admin.register(VideoComplementar)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data_criacao')
    list_filter = ('categoria',)