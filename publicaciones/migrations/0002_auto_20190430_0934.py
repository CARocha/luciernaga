# Generated by Django 2.1.1 on 2019-04-30 15:34

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnlaceVideoteca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Enlace Videoteca',
                'verbose_name_plural': 'Enlaces Videotecas',
            },
        ),
        migrations.AlterField(
            model_name='archivospublicaciones',
            name='archivo',
            field=models.FileField(upload_to='archivosPublicaciones/'),
        ),
        migrations.AlterField(
            model_name='publicaciones',
            name='portada',
            field=sorl.thumbnail.fields.ImageField(upload_to='publicaciones/'),
        ),
        migrations.AddField(
            model_name='enlacevideoteca',
            name='publicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.Publicaciones'),
        ),
    ]
