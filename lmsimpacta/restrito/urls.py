from django.urls import path

from . import views

app_name = 'restrito'
urlpatterns = [
    path('professor/', views.home_professor, name='home_professor'),
    path('aluno/', views.home_aluno, name='home_aluno')
]