from django.shortcuts import render
from django.views.generic.base import TemplateView, View

from django.contrib.auth.models import User

from .forms import SignUpForm

class AuthView(View):


    def post(self,request, *args, **kwargs):
        post = request.POST

        # print(post)
        context = {}

        form = SignUpForm(data=post, request=request)
        if form.is_valid():
            print('Form is valid!')
            user = User(password=post['password'], username=post['name'], email=post['email'])
            user.save()
            context['succesMessage'] = 'The user was created!'
        else:
            print('Errors in form!')
            context['form'] = form
            print(form.errors)



        return render(request, "auth.html", context)



    def get(self, request, *args, **kwargs):
        return render(request, "auth.html")




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['message'] = ':)'
        return context