from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    school = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=50)
    cirtifications = models.CharField(max_length=200)
    availability = models.CharField(max_length=200)
    picture = models.ImageField()
    website = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.name)
