from django.db import models
from apps.colaboradores.models import Colaborador


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=150, verbose_name='Motivo', help_text='motivo da hora extra')
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo

    class Meta:
        verbose_name_plural = "Registro de Horas Extras"

