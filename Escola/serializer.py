from rest_framework import serializers
from .models import *

class AlunoSeria(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields= ['id', 'nome', 'dataNasc']

class CursoSeria(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields= ['id', 'cod', 'nome', 'descricao', 'nivel']

class MatriculaSerial(serializers.ModelSerializer):
    class Meta:
        model= Matricula
        fields= '__all__'

class ListaMatriculaAlunoSeria(serializers.ModelSerializer):
    curso= serializers.ReadOnlyField(source= 'curso.nome') #ajuda a ler oq tem no campo desejado
    periodo= serializers.SerializerMethodField()  #mostrar o nome dado a choices
    class Meta:
        model= Matricula
        fields= ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaAlunosMatriculadosSeria(serializers.ModelSerializer):
    aluno_nome= serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model= Matricula
        fields= ['aluno_nome']

