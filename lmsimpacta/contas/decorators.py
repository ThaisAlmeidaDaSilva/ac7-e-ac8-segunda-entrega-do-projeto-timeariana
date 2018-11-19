from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib import messages

def usuario_e_professor(function):

    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.tipo != 'P':
            messages.error(request, 'Você não está autorizado a usar essa opção!')
            return redirect('core:home')
        else:
            return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def usuario_e_aluno(function):

    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.tipo != 'A':
            messages.error(request, 'Você não está autorizado a usar essa opção!')
            return redirect('core:home')
        else:
            return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap