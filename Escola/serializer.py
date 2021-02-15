from rest_framework import serializers
from .models import *

class AlunoSeria(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields= ['id', 'nome', 'dataNasc']

class CursoSeria(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields= ['id', 'cod', 'nome', 'descricao']