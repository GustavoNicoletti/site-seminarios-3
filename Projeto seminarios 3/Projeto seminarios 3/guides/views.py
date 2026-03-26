from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import GuiaRapido
from django.shortcuts import render, redirect
from .forms import GuiaRapidoForm
@login_required
def lista_guia(request):
    itens = GuiaRapido.objects.all().order_by('-data_criacao')
    return render(request, 'guides/lista_guia.html', {'itens': itens})

@login_required
def detalhe_guia(request, pk):
    item = get_object_or_404(GuiaRapido, pk=pk)
    return render(request, 'guides/detalhe_guia.html', {'item': item})

@login_required
def cadastrar_guia(request):
    if request.method == "POST":
        form = GuiaRapidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_guia')
    else:
        form = GuiaRapidoForm()
    return render(request, 'guides/cadastrar_guia.html', {'form': form})

@login_required
def excluir_guia(request, pk):
    # Busca o guia ou retorna erro 404
    item = get_object_or_404(GuiaRapido, pk=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('lista_guia')
        
    return render(request, 'guides/excluir_guia.html', {'item': item})