from django.conf.urls import url
import job.views

urlpatterns =[
    url(r'^all-job-list/$', job.views.all_job_list, name='all-job-list'),
    url(r'^detail/(?P<id>[0-9]+)/$', job.views.job_detail, name='job-detail'),
    url(r'^applicant/(?P<job_id>[0-9]+)/$', job.views.job_applicant, name='job-applicant'),
    url(r'^cv-download/(?P<slug>[a-zA-Z0-9_-]+)/$',job.views.cv_download_view,name='download'),
    url(r'^search-job/$', job.views.search_job, name='search-job'),
    url(r'^trial-job-post/$', job.views.trial_job_post, name='trial_job_post'),


]