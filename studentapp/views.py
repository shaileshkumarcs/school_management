from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class StudentDashboard(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(StudentDashboard, self).get_context_data(*args, **kwargs)
        return context