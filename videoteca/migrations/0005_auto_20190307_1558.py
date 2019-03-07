# Generated by Django 2.1.1 on 2019-03-07 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoteca', '0004_auto_20190307_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videotecas',
            name='idioma',
        ),
        migrations.AddField(
            model_name='videotecas',
            name='idioma',
            field=models.ManyToManyField(to='videoteca.Idiomas'),
        ),
        migrations.AlterField(
            model_name='videotecas',
            name='pais_prod',
            field=models.ManyToManyField(blank=True, related_name='pais_produccion', to='videoteca.Pais', verbose_name='Pais de producción'),
        ),
        migrations.AlterField(
            model_name='videotecas',
            name='pais_ref',
            field=models.ManyToManyField(blank=True, related_name='pais_referidos', to='videoteca.Pais', verbose_name='Pais de referidos'),
        ),
    ]