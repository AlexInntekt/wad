from django.shortcuts import render
from django.views.generic.base import TemplateView, View
# Create your views here.

class AuthView(View):


    def post(self,request, *args, **kwargs):
        print(request)
        print('\n\n\n')

        post = request.POST

        print(post)

        return render(request, "auth.html")

    def get(self, request, *args, **kwargs):
        return render(request, "auth.html")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['message'] = ':)'
        return context