from django.shortcuts import render, render_to_response
from .models import JobPost, JobCategory, JobApplication
from employer.models import CompanyProfile
from student.models import StudentProfile
from .forms import JobApplyForm, JobSearchForm, JobPostForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib import messages


def all_job_list(request):
    form = JobSearchForm()
    all_jobs = JobPost.objects.all()
    context = {'allJobs': all_jobs, 'form': form}
    return render(request, 'job/all-job-list.html', context)


def job_detail(request, id):
    form = JobApplyForm()
    job = JobPost.objects.get(pk=id)
    if request.method == 'POST':
        form = JobApplyForm(request.POST, request.FILES)
        applicant = StudentProfile.objects.get(user=request.user)
        if form.is_valid():
            cv = form.cleaned_data['cv']
            application = JobApplication()
            application.job = job
            application.applicant = applicant
            application.cv = cv
            application.save()
            messages.success(request, 'Thank you to apply job')
            return HttpResponseRedirect(reverse('all-job-list'))
    context = {'job': job, 'form':form, 'job_id':id,}
    return render(request, 'job/job_detail.html', context)


def job_applicant(request, job_id):
    applications = JobApplication.objects.filter(job__pk=job_id)
    job_name = JobPost.objects.get(pk=job_id).title
    context = {'applications': applications, 'jobName': job_name}
    return render(request, 'job/job-applicant-list.html', context)


def cv_download_view(request, slug):
    application = JobApplication.objects.get(pk=slug)
    filename = application.cv.file.name.split('/')[-1]
    response = HttpResponse(application.cv.file, content_type='application/liquid')
    response['Content-Disposition'] = 'attachment; filename=%s'%filename

    return response


def search_job(request):
    form = JobSearchForm()
    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        location = request.POST.get('location')
        job_posts = JobPost.objects.filter(Q(title__icontains=job_title) | Q(summery__icontains=job_title), location__icontains=location)
        context = {'job_posts': job_posts, 'form': form}
        return render(request, 'job/search-job-result.html', context)
    context = {'form':form}
    return render(request, 'job/search-job-result.html', context)


def trial_job_post(request):
    form = JobPostForm()
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job_post = form.save(commit=False)
            job_post.posted_by = request.user
            job_post.company = request.user.companyprofile
            job_post.save()
            company = CompanyProfile.objects.get(user=request.user)
            company.post_free_job = True
            company.save()
            return HttpResponseRedirect(reverse('employer_dashboard'))
    context = {'form': form}
    return render(request, 'job/trial_job_post_form.html', context)


def post_job(request):
    if request.user.companyprofile.verified:
        form = JobPostForm()
        if request.method == 'POST':
            form = JobPostForm(request.POST)
            if form.is_valid():
                job_post = form.save(commit=False)
                job_post.posted_by = request.user
                job_post.company = request.user.companyprofile
                job_post.save()
                company = CompanyProfile.objects.get(user=request.user)
                company.post_free_job = True
                company.save()
                return HttpResponseRedirect(reverse('employer_dashboard'))
        context = {'form': form}
        return render(request, 'job/job_post.html', context)
    else:
        context = {'error':'Verify your id to post job'}
        return render(request, 'job/job_post.html', context)


def delete_job(request, id):
    try:
        JobPost.objects.get(id=id).delete()
        messages.success(request, 'Job post deleted successfully')
        return HttpResponseRedirect(reverse('employer_dashboard'))
    except Exception as e:
        err = str(e)
        messages.error(request, err)
        return HttpResponseRedirect(reverse('employer_dashboard'))
