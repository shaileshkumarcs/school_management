from django.conf.urls import url

from .views import StudentDashboard

urlpatterns = [
    url(r'^', StudentDashboard.as_view(), name="student-dashboard"),
]

#deepak@mobilecoderz.com