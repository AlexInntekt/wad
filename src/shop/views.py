from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.db.models import Q

from .models import Item


class CartView(TemplateView):
    template_name = 'cart.html'

class CheckoutView(TemplateView):
    template_name = 'checkout.html'

class ConfirmPayView(TemplateView):
    template_name = 'confirm_pay.html'

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
                keyword = filters["searchname"]

                print("General search.")
                Qd = Q()

                Qd |= Q(name__icontains=keyword)
                Qd |= Q(brand__icontains=keyword)
                Qd |= Q(data__icontains=keyword)

                queryset = queryset.filter(Qd)

            except Exception as e:
                pass  
        else:  
            try:
                Qd = Q()

                print(filters)

                name = filters['name']
                brand = filters['brand']
                
                if(name != ''):
                    print("\n\n\n\n\nasd")
                    Qd &= Q(name__icontains=name)
                    # queryset = queryset.filter(Qd)

                if(brand != ''):
                    Qd &= Q(brand__icontains=brand)


                queryset = queryset.filter(Qd)

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