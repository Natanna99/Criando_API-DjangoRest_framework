from django.db import models

class Aluno(models.Model):
    nome= models.CharField(max_length= 35)
    dataNasc= models.DateField()

    def __str__(self):
        return '{} - {}'.format(self.nome, self.dataNasc)

class Curso(models.Model):
    Nivel= (
        ('B', "Basico"),
        ('I', 'Intermediario'),
        ('A', 'Avanaçado')
    )
    cod= models.CharField(max_length= 5)
    nome= models.CharField(max_length= 50)
    descricao= models.TextField(max_length= 300)
    nivel =  models.CharField(max_length= 2, choices= Nivel, blank= False, null= False, default= 'B')

    def __str__(self):
        return '{} - {}'.format(self.cod, self.nome)



