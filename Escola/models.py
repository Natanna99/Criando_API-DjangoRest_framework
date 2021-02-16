from django.db import models
from . import choices
class Aluno(models.Model):
    nome= models.CharField(max_length= 35)
    dataNasc= models.DateField()

    def __str__(self):
        return '{} - {}'.format(self.nome, self.dataNasc)

class Curso(models.Model):
    Nivel = choices.Nivel
    cod= models.CharField(max_length= 5)
    nome= models.CharField(max_length= 50)
    descricao= models.TextField(max_length= 300)
    nivel =  models.CharField(max_length= 2, choices= Nivel, blank= False, null= False, default= 'B')

    def __str__(self):
        return '{} - {}'.format(self.cod, self.nome)


class Matricula(models.Model):
    Periodo= choices.PERIODO
    aluno= models.ForeignKey(Aluno, on_delete= models.CASCADE)
    curso= models.ForeignKey(Curso, on_delete= models.CASCADE)
    periodo= models.CharField(max_length=2, choices= Periodo, blank=False, null=False, default= 'M')

    def __str__(self):
        return '{} - {}'.format(self.aluno.nome, self.curso.nome)




