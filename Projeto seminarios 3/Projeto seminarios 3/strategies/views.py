from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Estrategia
from .forms import EstrategiaForm


@login_required
def home(request):
    return render(request, 'strategies/home.html')


@login_required
def lista_estrategias(request):
    itens = Estrategia.objects.all().order_by('-id')
    return render(request, 'strategies/lista_estrategias.html', {'itens': itens})


@login_required
def detalhe_estrategia(request, pk):
    item = get_object_or_404(Estrategia, pk=pk)
    return render(request, 'strategies/detalhe_estrategia.html', {'item': item})


@login_required
def cadastrar_estrategia(request):
    if request.method == 'POST':
        form = EstrategiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estrategias')
    else:
        form = EstrategiaForm()

    return render(request, 'strategies/cadastrar_estrategia.html', {'form': form})


@login_required
def excluir_estrategia(request, pk):
    item = get_object_or_404(Estrategia, pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('lista_estrategias')

    return render(request, 'strategies/excluir_estrategia.html', {'item': item})