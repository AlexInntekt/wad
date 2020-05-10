from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Item


class DetailView(DetailView):
    template_name = 'detail.html'
    model = Item

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context



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

        if "searchname" in filters:
            try:
                print("aoleooooooooooooo")
            except Exception as e:
                pass  
        else:  
            try:
                part_name = filters['part_name']
                car = filters['car']
                model = filters['model']
                # production_year = 'production_year'
                # fuel_type = 'fuel_type'

                # if(part_name!=''):
                #     queryset = queryset.filter(Q(car_band__contains=part_name) | Q(car_model__contains=part_name) | Q(name__contains=part_name))
                # if(car!=''):
                queryset = queryset.filter(name__contains=car)
            # if(model!=''):
            #     queryset = queryset.filter(Q(car_band__contains=model) | Q(car_model__contains=model) | Q(name__contains=model))
            # if(fuel_type!=''):
            #     queryset = queryset.filter(name__contains=fuel_type)

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