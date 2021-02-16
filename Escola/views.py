#from django.http import JsonResponse
from .models import *
from rest_framework import viewsets, generics
from .serializer import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewsets(viewsets.ModelViewSet):
    queryset= Aluno.objects.all()
    serializer_class = AlunoSeria
    #authentication_classes= [BasicAuthentication]
    #permission_classes=[IsAuthenticated]

class CursosViewsets(viewsets.ModelViewSet):
    queryset= Curso.objects.all()
    serializer_class= CursoSeria

class MatriculaViewsets(viewsets.ModelViewSet):
    queryset= Matricula.objects.all()
    serializer_class= MatriculaSerial

class ListaMatriAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset= Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class= ListaMatriculaAlunoSeria

class ListaAlunosEmCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset= Matricula.objects.filter(curso_id= self.kwargs['pk'])
        print(queryset, 'QUERY')
        return queryset
    serializer_class= ListaAlunosMatriculadosSeria



#def Alunos(request):
    #if request.method == "GET":
        #aluno = {'id': 1, 'nome': 'Natanna'}
        #return JsonResponse(aluno)


