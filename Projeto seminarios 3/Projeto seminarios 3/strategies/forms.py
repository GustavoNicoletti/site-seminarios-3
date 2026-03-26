from django import forms
from .models import Estrategia

class EstrategiaForm(forms.ModelForm):
    class Meta:
        model = Estrategia
        fields = [
            'titulo',
            'descricao',
            'publico_alvo',
            'objetivo',
            'passo_a_passo',
            'materiais',
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Estratégia para organização da rotina'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descreva a estratégia de forma resumida'
            }),
            'publico_alvo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Educação infantil, ensino fundamental...'
            }),
            'objetivo': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Qual é o objetivo da estratégia?'
            }),
            'passo_a_passo': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Explique como aplicar a estratégia'
            }),
            'materiais': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Liste os materiais necessários'
            }),
        }