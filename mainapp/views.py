from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

def home(request):
    return render(request,'home.html',{})

class HomeView(View):
    def get(self,request, *args, **kwargs):
        context = {}
        return render(request,'home.html',context)

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self,*args, **kwargs):
        context = super(HomeTemplateView,self).get_context_data(*args, **kwargs)
        return context