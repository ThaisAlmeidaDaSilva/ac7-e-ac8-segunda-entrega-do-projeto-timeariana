from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="home"),
    path('contato/', views.contato, name="contato"),
    path('entrar/', views.entrar, name="entrar"),
    path('registrar/', views.registrar, name='registrar'),
    path('sair/', views.sair, name="sair")
]