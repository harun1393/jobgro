from django import forms
from .models import StudentProfile
from django.contrib.auth.models import User


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email')


class ProfileEditForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    school = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    cirtifications = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    availability = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    website = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    linkedin = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
        model = StudentProfile
        exclude = ('user',)