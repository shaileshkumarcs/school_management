"""nutantech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from mainapp.views import Home,Dashboard,AdminSignUpView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('accounts/', include('django.contrib.auth.urls')),
    url('accounts/admin/', AdminSignUpView.as_view(), name='admin_signup'),

    # For Home Page Redirect and mainapp urls
    url(r'^$', Home.as_view(), name="home"),
    url(r'^dashboard/$', Dashboard.as_view(), name="dashboard"),

    url(r'^adminapp/', include('adminmanage.urls', namespace='adminapp')),
    url(r'^mainapp/', include('mainapp.urls', namespace='mainapp')),
    url(r'^student/', include('studentapp.urls', namespace='student')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
