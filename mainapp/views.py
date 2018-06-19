from django.contrib.auth import login
from django.views.generic import TemplateView, CreateView
from django.contrib import messages

from django.shortcuts import redirect,render

from .forms import AdminSignUpForm
from .models import User

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
                return redirect("student:student-dashboard")
            elif request.user.is_admin:
                return redirect("adminapp:admin-dashboard")
        else:
            return redirect("/accounts/login")

        return render(request, 'home.html', {})

class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Admin Created Successfully!')
        return redirect('admin_signup')