from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import Item

class ListView(generic.ListView):
    template_name = 'list.html'

    def get_queryset(self):
        return Item.objects.all()

class SearchView(TemplateView):
    template_name = 'search.html'

    