# Generated by Django 2.2.7 on 2019-12-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='nome completo', max_length=150, verbose_name='Colaborador')),
            ],
            options={
                'verbose_name_plural': 'Colaboradores',
            },
        ),
    ]
