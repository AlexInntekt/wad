from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.db.models import Q

# from django.views.generic.edit import FormMixin
from PIL import Image, ImageOps
from .models import Item, Review, Category, Image, CategoryImage


class EditCategoryAdminView(TemplateView):
    template_name = 'edit_category.html'

    def get(self, request, *args, **kwargs):
        print("get")
        category = Category.objects.get(id=kwargs['id'])
        context = {}
        context['curent_category'] = category

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print("patch")
        update = request.POST
        image_data = request.FILES
        print("\n\n\n\n\n")
        

        try:
            delete = update['delete']
            Category.objects.get(id=kwargs['id']).delete()
            return redirect('adminview')
        except Exception:
            pass
            
        name = update['name']
        category = Category.objects.get(id=kwargs['id'])
        category.name = name
        category.save()

        if 'image' in image_data:

            image = CategoryImage.objects.filter(category__id=category.id).first()
            image.image = image_data['image']
            image.category = category
            image.save()

        context = {}
        context['curent_category'] = category

        return render(request, self.template_name, context)


class AddCategoryAdminView(TemplateView):
    template_name = 'add_category.html'

    def post(self, request, *args, **kwargs):
        post = request.POST
        image_data = request.FILES
        print("\n\n\n\n\n")
        name = post['name']

        new_category = Category()
        new_category.name = name
        new_category.save()

        new_image = CategoryImage()
        new_image.image = image_data['image']
        new_image.category = new_category
        new_image.save()

        return render(request, self.template_name, {})


class EditItemAdminView(TemplateView):
    template_name = 'edit_item.html'

    def get(self, request, *args, **kwargs):

        context = {}

        context['categories'] = Category.objects.all()
        context['item'] = Item.objects.get(id=kwargs['id'])

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        post = request.POST
        image_data = request.FILES
        print("\n\n\n\n\n")
        # print(post)
        # print(image_data['image'])

        dynamic_fields = {}

        try:
            delete = post['delete']
            Item.objects.get(id=kwargs['id']).delete()
            return redirect('adminview')
        except Exception as e:
            print(e)

        # print(post)
        for key,value in post.items():
            # print(value)
            if key not in ['name','brand','price','stock','category','engine', 'csrfmiddlewaretoken'] and value != '':
                print("{}:{} \n".format(key,value))
                dynamic_fields[key] = value

        name = post['name']
        brand = post['brand']
        price = post['price']
        stock = post['stock']
        category = post['category']
        category = Category.objects.filter(name__icontains=category).first()
        data = dynamic_fields

        new_item = Item.objects.get(id=kwargs['id'])
        new_item.name = name
        new_item.brand = brand
        new_item.price = price
        new_item.stock = stock
        new_item.category = category
        new_item.data = data

        new_item.save()

        # for image in images:
        if 'image' in image_data:
            new_image = Image()
            new_image.image = image_data['image']
            new_image.item = new_item
            new_image.save()

        context = {}

        context['categories'] = Category.objects.all()
        context['item'] = Item.objects.get(id=kwargs['id'])


        return render(request, self.template_name, context)

class AddItemAdminView(TemplateView):
    template_name = 'add_item.html'

    def get(self, request, *args, **kwargs):

        context = {}

        context['categories'] = Category.objects.all()

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        post = request.POST
        image_data = request.FILES
        print("\n\n\n\n\n")
        # print(post)
        # print(image_data['image'])

        dynamic_fields = {}

        # print(post)
        for key,value in post.items():
            # print(value)
            if key not in ['name','brand','price','stock','category','engine', 'csrfmiddlewaretoken'] and value != '':
                print("{}:{} \n".format(key,value))
                dynamic_fields[key] = value

        name = post['name']
        brand = post['brand']
        price = post['price']
        stock = post['stock']
        category = post['category']
        category = Category.objects.filter(name__icontains=category).first()
        data = dynamic_fields

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = Item.objects.all()
        categories = Category.objects.all()
        context['items'] = items
        context['categories'] = categories

        return context

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
        categories = Category.objects.all()
        context['categories'] = categories

        return context

    def get_queryset(self, *args, **kwargs):
        # print(kwargs)
        queryset = Item.objects.all()

        by_category = ''
        filters = self.request.GET

        try:
            by_category = self.request.resolver_match.kwargs['category']
        except Exception:
            pass

        # print(args)
        # print(kwargs)
        # print(self.request.__dict__)
        # print(self.request.resolver_match.kwargs['category'])

        if "searchname" in filters:
            print("\n General search. \n")
            try:
                keyword = filters["searchname"]

                Qd = Q()

                Qd |= Q(name__icontains=keyword)
                Qd |= Q(brand__icontains=keyword)
                Qd |= Q(data__icontains=keyword)

                queryset = queryset.filter(Qd)

            except Exception as e:
                pass  

        elif by_category != '':
            Qd = Q()
            print("\n\n Filtering by category \n\n")
            Qd &= Q(category__name__icontains=by_category)

            queryset = queryset.filter(Qd)

        else:  
            try:
                Qd = Q()

                name = filters['name']
                brand = filters['brand']
                
                if(name != ''):
                    print("Searching by name.")
                    Qd &= Q(name__icontains=name)
                    # queryset = queryset.filter(Qd)

                if(brand != ''):
                    print("Searching by brand.")
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