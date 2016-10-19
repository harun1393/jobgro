from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout


def student_register(request):
    form = UserForm
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            if password == re_password:
                user.password = make_password(password)
                user.type = 'std'
                user.save()
                return HttpResponseRedirect(reverse('update_std_profile'))
            else:
                errmsg = "Password Does not match"
                context = {'form': form, 'errMsg': errmsg}
                return render(request, 'account/register_usr.html', context)
    context = {'form': form}
    return render(request, 'account/register_usr.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
