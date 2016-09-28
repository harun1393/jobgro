from django.conf.urls import url
import job.views

urlpatterns =[
    url(r'^all-job-list/$', job.views.all_job_list, name='all-job-list'),
    url(r'^detail/(?P<id>[0-9]+)/$', job.views.job_detail, name='job-detail'),

]