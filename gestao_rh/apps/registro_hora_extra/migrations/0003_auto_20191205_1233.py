# Generated by Django 2.2.7 on 2019-12-05 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0002_registrohoraextra_colaborador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrohoraextra',
            name='colaborador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='colaboradores.Colaborador'),
        ),
    ]