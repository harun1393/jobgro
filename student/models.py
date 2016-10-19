from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150,  null=True, blank=True)
    school = models.CharField(max_length=150,null=True, blank=True )
    state = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    zip_code = models.CharField(max_length=50, blank=True, null=True)
    cirtifications = models.CharField(max_length=200, blank=True, null=True)
    availability = models.CharField(max_length=200, blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)
    descripton = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return str(self.name)
