from django.db import models
from apps.colaboradores.models import Colaborador

class Documento(models.Model):
    descricao = models.CharField(max_length=100, verbose_name='Documento', help_text='documento')
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Documentos"
