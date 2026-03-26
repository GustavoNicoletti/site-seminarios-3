from django import forms
from .models import GuiaRapido

class GuiaRapidoForm(forms.ModelForm):
    class Meta:
        model = GuiaRapido
        fields = ['titulo', 'conteudo', 'dicas', 'acoes_rapidas']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Como lidar com crises'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'dicas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Dicas práticas...'}),
            'acoes_rapidas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'O que fazer agora...'}),
        }