from django.conf.urls import url

from .views import AdminDashboard, AdminAddClass

urlpatterns = [
    url(r'^addclass/$', AdminAddClass.as_view(), name="admin-addclass"),
    url(r'^$', AdminDashboard.as_view(), name="admin-dashboard"),
]