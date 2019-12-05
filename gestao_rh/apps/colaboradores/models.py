from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Colaborador(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Colaborador', help_text='Nome completo')
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    departamento = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Colaboradores"