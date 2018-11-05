from django.contrib import admin
from import_export import resources
from .models import Generos, Idiomas, Temas, Videotecas, Series, Pais
from import_export.admin import ImportExportModelAdmin

class VideotecasResource(resources.ModelResource):
    class Meta:
        model = Videotecas
        exclude = ('slug', )

class GenerosResource(resources.ModelResource):
    class Meta:
        model = Generos

class IdiomasResource(resources.ModelResource):
    class Meta:
        model = Idiomas

class TemasResource(resources.ModelResource):
    class Meta:
        model = Temas

class SeriesResource(resources.ModelResource):
    class Meta:
        model = Series

class PaisResource(resources.ModelResource):
    class Meta:
        model = Pais

class GenerosAdmin(ImportExportModelAdmin):
    resource_class = GenerosResource

class IdiomasAdmin(ImportExportModelAdmin):
    resource_class = IdiomasResource

class TemasAdmin(ImportExportModelAdmin):
    resource_class = TemasResource

class SeriesAdmin(ImportExportModelAdmin):
    resource_class = SeriesResource

class PaisAdmin(ImportExportModelAdmin):
    resource_class = PaisResource

class VideotecasAdmin(ImportExportModelAdmin):
    resource_class = VideotecasResource

# Register your models here.
admin.site.register(Generos, GenerosAdmin)
admin.site.register(Idiomas, IdiomasAdmin)
admin.site.register(Temas, TemasAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Videotecas, VideotecasAdmin)
