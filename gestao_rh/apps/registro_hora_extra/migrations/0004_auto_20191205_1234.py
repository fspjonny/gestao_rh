# Generated by Django 2.2.7 on 2019-12-05 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0003_auto_20191205_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrohoraextra',
            name='colaborador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='colaboradores.Colaborador'),
        ),
    ]
