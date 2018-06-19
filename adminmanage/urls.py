from django.conf.urls import url

from .views import AdminDashboard

urlpatterns = [
    url(r'^', AdminDashboard.as_view(), name="admin-dashboard"),
]