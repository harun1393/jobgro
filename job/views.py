from django.shortcuts import render
from .models import JobPost, JobCategory


def all_job_list(request):
    all_jobs = JobPost.objects.all()
    print all_jobs
    context = {'allJobs': all_jobs}
    return render(request, 'job/all-job-list.html', context)


def job_detail(request,id):
    job = JobPost.objects.get(pk=id)
    print job.company.name
    context = {'job': job}
    return render(request, 'job/job_detail.html', context)
