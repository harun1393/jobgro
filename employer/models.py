from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class CompanyProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name= models.CharField(max_length=150, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    state = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    field = models.CharField(max_length=150, blank=True, null=True)
    type = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()
    post_free_job = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.name)


