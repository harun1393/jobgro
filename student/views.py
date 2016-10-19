from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from student.models import StudentProfile
from job.models import JobPost
from django.shortcuts import get_object_or_404
from .forms import ProfileEditForm
from django.views.generic import TemplateView
import forms
from django.conf import settings
from job.forms import  JobSearchForm



def home(request):
    student_list = StudentProfile.objects.all().order_by('-id')[:8]
    job_list = JobPost.objects.all().order_by('-id')[:8]
    context = {'student_list':student_list, 'job_list':job_list}
    return render(request, 'home.html', context)


def student_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        userName = authenticate(email=email, password=password)
        if userName:
            if userName.is_active:
                if userName.type == 'std':
                    login(request, userName)
                    return HttpResponseRedirect(reverse('student_profile'))
                else:
                    error = "You'r not a student"
                    context = {"errMsg": error}
                    return render(request, 'student/student_login.html', context)
            else:
                error = "Account Deactivated"
                context = {"errMsg": error}
                return render(request, 'student/student_login.html', context)
        else:
            # context = RequestContext(request)
            error = "Incorrect Email or password is "
            context = {"errMsg": error}
            return render(request, 'student/student_login.html', context)
    else:
        return render(request, 'student/student_login.html')


# Student Profile page
def student_profile(request):
    user = request.user
    try:
        profile = user.studentprofile
    except StudentProfile.DoesNotExist:
        profile = StudentProfile(user=request.user)
    context = {'profile':profile}
    return render(request, 'student/studentProfile.html', context)






def update_std_profile(request):
    user = request.user
    try:
        profile = user.studentprofile
    except StudentProfile.DoesNotExist:
        profile = StudentProfile(user=user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponseRedirect(reverse('student_profile'))
    else:
        form = ProfileEditForm()
    context = {'profile_form': form}
    return render(request, 'student/stdprofedit_form.html', context)

