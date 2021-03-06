# Generated by Django 2.1.2 on 2018-11-04 15:22

import contas.models.usuario
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_auto_20181031_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=155, verbose_name='Nome Completo')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('celular', models.CharField(max_length=11, verbose_name='Celular')),
                ('ra', models.IntegerField(verbose_name='RA')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto')),
            ],
            options={
                'db_table': 'ALUNO',
            },
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=155, verbose_name='Nome Completo')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('celular', models.CharField(max_length=11, verbose_name='Celular')),
            ],
            options={
                'db_table': 'COORDENADOR',
            },
        ),
        migrations.CreateModel(
            name='CoordenadorUsuario',
            fields=[
            ],
            options={
                'verbose_name': 'coordenador',
                'verbose_name_plural': 'coordenadores',
                'proxy': True,
                'indexes': [],
            },
            bases=('contas.usuario',),
            managers=[
                ('objects', contas.models.usuario.UsuarioManager()),
            ],
        ),
        migrations.AddField(
            model_name='coordenador',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='aluno',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
