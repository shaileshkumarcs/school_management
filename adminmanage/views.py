from django.shortcuts import render, redirect

from django.views.generic import TemplateView

# Create your views here.

class AdminDashboard(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated() and request.user.is_admin:
            print(request.user)
            return render(request, 'admindashboard.html',{})

        return redirect("/accounts/login")

class AdminAddClass(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated() and request.user.is_admin:
            return render(request, 'adminadd_class.html',{})

        return redirect("/accounts/login")