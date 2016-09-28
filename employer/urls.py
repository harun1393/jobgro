from django.conf.urls import url
import employer.views

urlpatterns =[
    url(r'^login', employer.views.employer_login, name='employer_login'),
    url(r'^register', employer.views.employer_register, name='employer_register'),
    url(r'^dashboard', employer.views.employer_dashboard, name='employer_dashboard'),
    url(r'^profile/$', employer.views.company_profile, name='company_profile'),
    url(r'^profile_edit/$', employer.views.edit_company_profile, name='edit_company_profile'),
]