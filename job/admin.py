from django.contrib import admin
from .models import JobPost
from .models import JobCategory


admin.site.register(JobCategory)
admin.site.register(JobPost)
