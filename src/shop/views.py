from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.shortcuts import redirect
from django.views.generic.list import ListView

from .models import Item



class ListView(ListView):
    template_name = 'list.html'
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Item.objects.all()

class SearchView(TemplateView):
    template_name = 'search.html'

    def get(self, request):
        return render(request, 'search.html')

    def post(self, request):
        return redirect('listview')