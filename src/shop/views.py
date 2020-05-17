from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.db.models import Q

# from django.views.generic.edit import FormMixin
from PIL import Image, ImageOps
from .models import Item, Review, Category, Image

class AddItemAdminView(TemplateView):
    template_name = 'add_item.html'

    def post(self, request, *args, **kwargs):
        post = request.POST
        image_data = request.FILES
        print("\n\n\n\n\n")
        print(post)
        print(image_data['image'])

        name = post['name']
        brand = post['brand']
        price = post['price']
        stock = post['stock']
        category = post['category']
        category = Category.objects.filter(name__icontains=category).first()
        data = {}

        new_item = Item()
        new_item.name = name
        new_item.brand = brand
        new_item.price = price
        new_item.stock = stock
        new_item.category = category
        new_item.data = data

        new_item.save()

        # for image in images:
        new_image = Image()
        new_image.image = image_data['image']
        new_image.item = new_item
        new_image.save()


        return render(request, self.template_name, {})

class AdminView(TemplateView):
    template_name = 'admin.html'

class CartView(TemplateView):
    template_name = 'cart.html'

class CheckoutView(TemplateView):
    template_name = 'checkout.html'

class ConfirmPayView(TemplateView):
    template_name = 'confirm_pay.html'

class DetailView(TemplateView):
    template_name = 'detail.html'
    # model = Item
    
    # def get_success_url(self):
    #     return reverse('post_detail', kwargs={'pk': self.object.id})

    # def get_context_data(self, **kwargs):
    #     context = super(DetailView, self).get_context_data(**kwargs)
    #     ## the context is a list of the tasks of the Project##
    #     ##THIS IS THE ERROR##
    #     # context['tasks'] = Task.object.filter(list=Project) <---->HERE ((work with Task.object.all() ))
    #     context['reviews'] = self.object.reviews.all()
    #     context['message'] = "bau"
    #     return(context)

    def post(self, request, *args, **kwargs):
        current_object = Item.objects.get(id=kwargs['id'])
        
        user = 'Anonymous'
        try:
            user = request.user
        except Exception:
            pass

        post = request.POST
        new_review = Review()
        new_review.text = post['message']
        new_review.author = user
        new_review.item = current_object
        new_review.save()

        obj = current_object
        reviews = obj.reviews.all()

        context = {}
        context['object'] = obj
        context['reviews'] = reviews

        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        obj = Item.objects.get(id=kwargs['id'])
        # reviews = Review.objects.filter(item__id=obj.id).first()
        reviews = obj.reviews.all()
        context = {}
        context['object'] = obj
        context['reviews'] = reviews
        return render(request, self.template_name, context)

class ContactView(TemplateView):
    template_name = 'contact.html'

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