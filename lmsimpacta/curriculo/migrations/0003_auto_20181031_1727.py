# Generated by Django 2.1.2 on 2018-10-31 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0002_auto_20181030_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinaofertada',
            name='data_fim',
            field=models.DateField(blank=True, null=True, verbose_name='Data Fim'),
        ),
        migrations.AlterField(
            model_name='disciplinaofertada',
            name='data_inicio',
            field=models.DateField(blank=True, null=True, verbose_name='Data Ínicio'),
        ),
    ]
