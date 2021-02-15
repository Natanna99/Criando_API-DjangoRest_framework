from django.http import JsonResponse
from .models import *
from rest_framework import viewsets
from .serializer import *

class AlunosViewsets(viewsets.ModelViewSet):
    queryset= Aluno.objects.all()
    serializer_class = AlunoSeria

class CursosViewsets(viewsets.ModelViewSet):
    queryset= Curso.objects.all()
    serializer_class= CursoSeria

#def Alunos(request):
    #if request.method == "GET":
        #aluno = {'id': 1, 'nome': 'Natanna'}
        #return JsonResponse(aluno)


