# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Noticias, Temas
from eventos.models import Eventos
from videoteca.models import Videotecas

# Create your views here.

class HomeView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticias.objects.all().order_by('-fecha')[:4]
        context['eventos'] = Eventos.objects.all().order_by('-fecha_inicio')[:8]
        context['videotecas'] = Videotecas.objects.all().order_by('-id')[:8]

        return context


class NoticiasList(ListView):
    template_name = 'lista_noticias.html'
    model = Noticias

class NoticiaDetailView(DetailView):
    model = Noticias
    template_name = 'blog_single.html'
    #context_object_name = 'nota'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_noticias'] = Noticias.objects.exclude(pk=self.object.pk).order_by('-fecha')[:3]
        context['temas'] = Temas.objects.all()

        return context


class EventoDetailView(DetailView):
    model = Eventos
    template_name = 'event_single.html'
    #context_object_name = 'nota'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_noticias'] = Noticias.objects.order_by('-fecha')[:3]
        context['temas'] = Temas.objects.all()

        return context
