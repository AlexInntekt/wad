from django.shortcuts import render
from django.views.generic import TemplateView

class SearchView(TemplateView):
	template_name = 'a.html'