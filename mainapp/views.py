from django.views.generic import TemplateView

from django.shortcuts import redirect,render

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        return  context

class Dashboard(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            if request.user.is_superuser:
                #return render(request, 'dashboard.html',{})
                return redirect("student:student-dashboard")
        else:
            return redirect("/accounts/login")

        return render(request, 'home.html', {})