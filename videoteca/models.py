# -*- coding: utf-8 -*-

from django.db import models
from django.template import defaultfilters
from sorl.thumbnail import ImageField

# Create your models here.

class Generos(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
        ordering = ('nombre',)

class Idiomas(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'
        ordering = ('nombre',)

class Temas(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'
        ordering = ['-id']

class SubTemas(models.Model):
    tema = models.ForeignKey(Temas, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Sub tema'
        verbose_name_plural = 'Sub Temas'
        ordering = ['-id']

class Coleccion(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Colleción'
        verbose_name_plural = 'Collecciones'

class Pais(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        ordering = ('nombre',)

class Series(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'serie'
        verbose_name_plural = 'series'
        ordering = ('nombre',)

class Videotecas(models.Model):
    cod_cat = models.CharField('Codigo categoría', max_length=50)
    #fecha = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, editable=False)
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE, null=True, blank=True)
    duracion = models.CharField('Duración' , max_length=150, null=True, blank=True)
    edicion = models.CharField('Edición', max_length=250, null=True, blank=True)
    fotografia = models.CharField('Fotografía', max_length=250, null=True, blank=True)
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    guion = models.CharField('Guión', max_length=250, null=True, blank=True)
    idioma = models.ManyToManyField(Idiomas)
    musica_original = models.CharField('Música original', max_length=250, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    pais_prod = models.ManyToManyField( Pais,
                            verbose_name='Pais de producción',  related_name='pais_produccion', blank=True)
    pais_ref = models.ManyToManyField(Pais,
                            verbose_name='Pais de referidos', related_name='pais_referidos', blank=True)
    produccion = models.CharField('Producción', max_length=250, null=True, blank=True)
    productora = models.CharField('Productora', max_length=250, null=True, blank=True)
    realizacion = models.CharField('Realización', max_length=250, null=True, blank=True)
    serie = models.ForeignKey(Series, on_delete=models.CASCADE, null=True, blank=True)
    sintesis = models.TextField('Síntesis', null=True, blank=True)
    subtitulos = models.CharField('Subtítulos', max_length=250, null=True, blank=True)
    temas = models.ManyToManyField(Temas, verbose_name='Temas principales', blank=True)
    subtema = models.ManyToManyField(SubTemas, verbose_name="Temas secundarios", blank=True )
    url_video = models.URLField(null=True, blank=True)
    imagen_portada = models.ImageField(null=True, blank=True)
    imagen_fill = models.ImageField(null=True, blank=True)
    anio = models.CharField('Año', max_length=50, null=True, blank=True)
    apoyo = models.CharField('Apoyo de', max_length=250, null=True, blank=True)

    def save(self, *args, **kwargs):
      self.slug = defaultfilters.slugify(self.titulo)
      super(Videotecas, self).save(*args, **kwargs)

    # def _tiene_guias(self, *args, **kwargs):
    #     if self.guiasdidacticas_set.count() > 0:
    #         return True
    #     return False
    # _tiene_guias.boolean = True

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Videoteca'
        verbose_name_plural = 'Videotecas'
        ordering = ['-id']

class EnlacePublicacion(models.Model):
    videoteca = models.ForeignKey(Videotecas, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250, null=True)
    url = models.URLField()

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Enlace publicación'
        verbose_name_plural = 'Enlaces publicaciones'





