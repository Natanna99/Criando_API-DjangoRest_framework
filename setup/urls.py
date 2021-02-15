from django.contrib import admin
from django.urls import path, include
from Escola.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewsets, basename="Alunos"),
router.register('cursos', CursosViewsets, basename="Cursos"),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))

]
