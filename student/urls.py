from django.conf.urls import url
import student.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    url(r'^sign_in/$', student.views.student_login, name='student_signin'),
    #url(r'^home/$', student.views.student_panel, name='student_panel'),
    url(r'^profile/$', student.views.student_profile, name='student_profile'),
    url(r'^std-profile/edit/$', student.views.update_std_profile, name='update_std_profile')
]