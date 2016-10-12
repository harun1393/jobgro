from django.contrib import admin
from .models import JobPost, JobApplication
from .models import JobCategory


admin.site.register(JobCategory)
admin.site.register(JobPost)
admin.site.register(JobApplication)
