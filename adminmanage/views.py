from django.shortcuts import render, redirect

from django.views.generic import TemplateView

# Create your views here.

class AdminDashboard(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return render(request, 'admindashboard.html',{})

        return redirect("/accounts/login")