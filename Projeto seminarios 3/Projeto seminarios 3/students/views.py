from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Aluno
from .forms import AlunoForm

@login_required
def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'students/lista_alunos.html', {'alunos': alunos})

@login_required
def cadastrar_aluno(request):
    if request.method == "POST":
        # request.FILES é obrigatório para upload de fotos
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm()
    return render(request, 'students/cadastrar_aluno.html', {'form': form})

@login_required
def excluir_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('lista_alunos')
    return render(request, 'students/excluir_alunos.html', {'aluno': aluno})

@login_required
def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == "POST":
        # request.FILES aqui permite alterar a foto existente
        form = AlunoForm(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'students/editar_aluno.html', {'form': form, 'aluno': aluno})

@login_required
def detalhe_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'students/detalhe_aluno.html', {'aluno': aluno})