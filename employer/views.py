from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from account.forms import UserForm
from django.contrib.auth.hashers import make_password
from .models import CompanyProfile
from .forms import CompanyProfileForm


def employer_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        userName = authenticate(email=email, password=password)
        if userName:
            if userName.type == 'emp':
                if userName.is_active:
                    login(request, userName)
                    return HttpResponseRedirect(reverse('employer_dashboard'))
                else:
                    error = "Your id Deactivated !"
                    context = {"errMsg": error}
                    return render(request, 'student/student_login.html', context)
            else:
                error = "You are not an Employer"
                context = {"errMsg": error}
                return render(request, 'student/student_login.html', context)
        else:
            # context = RequestContext(request)
            error = "Email or password incorrect"
            context = {"errMsg": error}
            return render(request, 'student/student_login.html', context)
    else:
        return render(request, 'employer/employer_login.html')

from job.models import JobPost
def employer_dashboard(request):
    jobPosts = JobPost.objects.filter(company__user=request.user)
    context = {'jobPosts':jobPosts}
    return render(request, 'employer/employer_dashboard.html', context)


def employer_register(request):
    form = UserForm
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password1 = form.cleaned_data['password']
            password2 = form.cleaned_data['re_password']
            if password1 == password2:
                user.password = make_password(password1) # Django default password hash
                user.type = 'emp'    # User type = employer
                user.save()
                return HttpResponseRedirect(reverse('employer_dashboard'))
            else:
                errmsg = "Password Does not match"
                context = {'form': form, 'errMsg':errmsg}
                return render(request, 'account/register_usr.html', context)
    context = {'form': form}
    return render(request, 'employer/register_employer.html', context)


def company_profile(request):
    user = request.user
    try:
        company = user.companyprofile
    except CompanyProfile.DoesNotExist:
        company = CompanyProfile(user=user)
    context = {'company': company}
    return render(request, 'employer/company_profile.html', context)


def edit_company_profile(request):
    user = request.user
    try:
        profile = user.companyprofile
        print profile
    except CompanyProfile.DoesNotExist:
        profile = CompanyProfile(user=user)
    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponseRedirect(reverse('company_profile'))
    else:
        form = CompanyProfileForm(instance=profile)
    context = {'form': form}
    return render(request, 'employer/edit_com_pro.html', context)