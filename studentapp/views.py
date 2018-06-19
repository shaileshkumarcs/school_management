from django.shortcuts import render, redirect

from django.views.generic import TemplateView

# Create your views here.

class StudentDashboard(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            if request.user.is_superuser:
                return render(request, 'studentdashboard.html',{})

        return redirect("/accounts/login")



# class StudentDashboard(TemplateView):
#     template_name = 'dashboard.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(StudentDashboard, self).get_context_data(*args, **kwargs)
#         return context