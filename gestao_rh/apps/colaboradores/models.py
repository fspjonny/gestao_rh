from django.db import models

class colaborador(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Colaborador', help_text='Nome completo')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Colaboradores"