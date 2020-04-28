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

    def get_queryset(self, **kwargs):
        # print(kwargs)
        queryset = Item.objects.all()

        filters = self.request.GET
        print(filters)

        try:
            part_name = filters['part_name']
            car = filters['car']
            model = 'model'
            production_year = 'production_year'
            fuel_type = 'fuel_type'

            if(part_name!=''):
                queryset = queryset.filter(name__contains=part_name)
            if(car!=''):
                queryset = queryset.filter(Q(car_band__contains=part_name) | Q(car_model__contains=part_name)) 
        except Exception as e:
            pass   

        return queryset

class SearchView(TemplateView):
    template_name = 'search.html'

    def get(self, request, **kwargs):
        return render(request, 'search.html')

    # def post(self, request, **kwargs):
    #     filters = request.POST

    #     return redirect('listview',{"filters":1})
    #     # return render(request, 'listview')