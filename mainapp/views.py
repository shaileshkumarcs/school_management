from django.shortcuts import render
from django.views import View

# Create your views here.

def home(request):
    return render(request,'home.html',{})

class HomeView(View):
    def get(self,request, *args, **kwargs):
        context = {}
        return render(request,'home.html',context)
