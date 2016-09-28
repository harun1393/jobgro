from django import forms
from .models import CompanyProfile


class CompanyProfileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    logo = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    field = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    type = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control col-md-7 col-xs-12'}))
    class Meta:
        model = CompanyProfile
        exclude = ('user', )
