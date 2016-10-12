"""jobgro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
import student.urls
import employer.urls
import account.urls
import job.urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^student/', include(student.urls)),
    url(r'^employer/', include(employer.urls)),
    url(r'^job/', include(job.urls)),
    url(r'^register/', include(account.urls)),
    url(r'^$',student.views.home, name='home'),
    url(r'^logout/$',account.views.logout_view, name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
