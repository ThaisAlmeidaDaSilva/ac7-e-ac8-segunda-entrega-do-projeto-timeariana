from datetime import datetime

from django.shortcuts import render, get_object_or_404

from .models import Curso, DisciplinaOfertada

# Create your views here.
def curso(request, sigla):
    curso = get_object_or_404(Curso, sigla=sigla)

    curso.semestres = range(1, curso.duracao+1)

    hoje = datetime.now()
    ano = hoje.year
    
    disciplinas = DisciplinaOfertada.objects.filter(
        ano=ano,
        curso=curso
    ).order_by("semestre")
    
    context = {
        'curso': curso,
        'ofertas': disciplinas
    }
    return render(request, 'curriculo/curso.html', context)

def disciplina(request, sigla, identificador):
    disciplina = {
        'nome': 'Tecnologias Web',
        'carga': '80 Horas',
        'descricao': 'Conceitos e fundamentos: Internet, Intranet e Extranet. Arquitetura Cliente-Servidor. Desenvolvimento de aplicações WEB Padrões Web. HTML (HyperText Markup Language) e CSS ( Cascading Style Sheets). Sintaxe, comandos JavaScript e integração com HTML. Noções de NodeJS. Python e Framework de Desenvolvimento.  Arquitetura Model-View-Controller; a camada de acesso a banco de dados; Padrão de endereçamento http; aspetos de segurança, componentização JQuery + AJAX.',
        'professor': 'Prof Yuri Dirickson'
    }
    context = {
        'disciplina':disciplina
    }
    return render(request, 'curriculo/disciplina.html', context)