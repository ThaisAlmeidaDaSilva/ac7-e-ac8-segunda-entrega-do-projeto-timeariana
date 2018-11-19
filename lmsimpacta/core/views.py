from datetime import datetime

from django.db import transaction
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from contas.forms import AlunoForm, UsuarioForm
from .forms import ContatoForm

# Create your views here.
def index(request):
    hoje = datetime.now()
    context = {
        'ano': hoje.year + 1,
        'semestre': 1 if hoje.month >= 6 else 2
    }
    return render(request, "index.html", context)

def contato(request):
    context = {}
    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Sua mensagem foi enviada com sucesso') 
        else:
            messages.error(request, 'Problemas ao enviar seu e-mail!')
    else:
        form = ContatoForm()

    context["form"] = form
    return render(request, 'contato.html', context)

def error404(request, exception=None):
    return render(request, 'error/404.html')

def sair(request):
    logout(request)
    return redirect('core:home')

def entrar(request):
    context = {}
    if request.POST:
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        usuario = authenticate(username=usuario, password=senha)
        if usuario:
            login(request, usuario)
            return redirect(usuario.get_absolute_url())
        else:
            messages.error(request, 'Usuário ou senha incorretos!')
    return render(request, 'entrar.html', context)

@transaction.atomic
def registrar(request):
    context = {}
    aluno_form = AlunoForm(request.POST or None)
    usuario_form = UsuarioForm(request.POST or None)
    if request.POST:
        if usuario_form.is_valid() and aluno_form.is_valid():
            usuario = usuario_form.save(commit=False)
            aluno = aluno_form.save(commit=False)
            usuario.tipo = 'A'
            aluno.usuario = usuario
            usuario.save()
            aluno.save()
            messages.success(request, 'Inscrito com sucesso, tente se logar agora')
            return redirect('core:home')

    context['aluno_form'] = aluno_form
    context['usuario_form'] = usuario_form
    return render(request, 'registrar.html', context)