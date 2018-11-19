from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from contas.decorators import usuario_e_professor, usuario_e_aluno

@login_required
@usuario_e_professor
def home_professor(request):
    return render(request, 'restrito/home.html')

@login_required
@usuario_e_aluno
def home_aluno(request):
    return render(request, 'restrito/home.html')
