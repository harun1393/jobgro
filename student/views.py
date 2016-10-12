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


def home(request):
    student_list = StudentProfile.objects.all()[:5]
    job_list = JobPost.objects.all()[:6]
    print job_list
    context = {'student_list':student_list, 'job_list':job_list}
    return render(request, 'home.html', context)


def student_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        userName = authenticate(email=email, password=password)
        print userName
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


def student_panel(request):
    print request.user
    context = {}
    return render(request, 'student/student_panel.html', context)


# Student Profile page
def student_profile(request):
    user = request.user
    try:
        profile = user.studentprofile
    except StudentProfile.DoesNotExist:
        profile = StudentProfile(user=request.user)
    context = {'profile':profile}
    return render(request, 'student/studentProfile.html', context)



# Class based view to manage EditProfile
'''
class EditStudentProfile(TemplateView):
    def get_objects(self, username):
        if username:
            user = get_object_or_404(settings.AUTH_USER_MODEL, username=username)
            try:
                profile = user.studentprofile
            except StudentProfile.DoesNotExist:
                profile = StudentProfile(user=user)
        else:
            user = settings.AUTH_USER_MODEL()
            profile = StudentProfile(user=user)
        return user, profile

    def get(self, request, username=None):
        print "get request"
        user, profile = self.get_objects(username)
        return self.render_to_response({
            'username':username,
            #'user_form':forms.UserEditForm(instance=user),
            'profile_form': forms.ProfileEditForm(instance=profile)
        })

    def post(self, request, ):
        #user, profile = self.get_objects()
        profile_form = forms.ProfileEditForm(request.POST)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            #profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse('student_profile'))
        context = {'profile_form':profile_form}
        return self.render_to_response(context)
'''


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

