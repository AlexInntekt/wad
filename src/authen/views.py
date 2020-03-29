from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import SignUpForm, SignInForm

class AuthView(View):


    def post(self,request, *args, **kwargs):
        post = request.POST
        whichForm = post['whichForm']
        print(whichForm)
        context = {}

        if(whichForm=='signup'):
            form = SignUpForm(data=post, request=request)
            if form.is_valid():
                print('Form is valid!')
                try:
                    password = form.cleaned_data.get('password')
                    username = form.cleaned_data.get('name')
                    email = form.cleaned_data.get('email')
                    user = User.objects.create_user(username=username,
                                 email=email,
                                 password=password)
                    user.save()
                    context['succesMessage'] = 'The user was created!'
                except Exception as e:
                    context['errorMessage'] = e
            else:
                print('Errors in form!')
                context['form'] = form
                print(form.errors)



        if(whichForm=='signin'):
            form = SignInForm(data=post, request=request)

            if form.is_valid():
                print('Form is valid!')

                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                username = User.objects.get(email=email).username

                print(username)
                print(password)

                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request,user)
                else:
                    context['errorMessage'] = 'Logare nereusita!'

                # try:
                #     user = authenticate(email=email, password=password)
                #     if user is not None:
                #         if user.is_active:
                #             login(request, user)
                #             print('User authenticated!')
                #             # return HttpResponseRedirect('/home/')

                # except Exception as e:
                #     print(e)
                #     context['errorMessage'] = e

                    

            else:      
                print('Errors in form!')
                print(form.errors)
                context['form'] = form
                    


        return render(request, "auth.html", context)



    def get(self, request, *args, **kwargs):
        return render(request, "auth.html")




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['message'] = ':)'
        return context