from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Departamento', help_text='Nome do departamento.')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Departamentos'
