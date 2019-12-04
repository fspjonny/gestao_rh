from django.db import models

class Documento(models.Model):
    descricao = models.CharField(max_length=100, verbose_name='Documento', help_text='documento')

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Documentos"
