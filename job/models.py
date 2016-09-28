from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from employer.models import CompanyProfile


class JobCategory(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class JobPost(models.Model):
    title = models.CharField(max_length=150)
    post_date = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    company = models.ForeignKey(CompanyProfile)
    category = models.ForeignKey(JobCategory)
    summery = models.TextField()

    def __unicode__(self):
        return self.title