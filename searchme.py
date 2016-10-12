import json, requests
from job.models import JobPost
settings.configure()

post = Jobpost.objects.all()

print post
