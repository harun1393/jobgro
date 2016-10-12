from django import forms
from .models import JobPost, JobCategory


class JobApplyForm(forms.Form):
    cv = forms.FileField(widget=forms.FileInput())


class JobSearchForm(forms.Form):
    job_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Name'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}))


class JobPostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    category = forms.ModelChoiceField(queryset=JobCategory.objects.all(), widget=forms.Select(attrs={'class':'form-control col-md-7 col-xs-12'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    summery = forms.CharField(widget=forms.Textarea(attrs={'class': 'editor-wrapper placeholderText col-md-7 col-xs-12', 'id': 'editor'}))

    class Meta:
        model = JobPost
        exclude = ('post_date', 'posted_by', 'company')
