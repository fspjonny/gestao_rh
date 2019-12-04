from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome da Empresa", help_text="ex: FSP Sistemas LTDA.")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Empresas"
