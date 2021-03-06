"""luciernaga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site
from noticias.views import AcercaView
from django.views.generic import TemplateView

admin.site.site_title = "Sitio Administrativo de Luciérnaga"
admin.site.site_header = "Luciérnaga Administración"

urlpatterns = [
    #path('jet/', include('jet.urls', 'jet')),
    path('', include('noticias.urls')),
    path('admin/', admin.site.urls),
    path('admin/filebrowser/', site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('acerca-de/', AcercaView.as_view()),
    path('404/', TemplateView.as_view(template_name="404.html"), name="404")

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
