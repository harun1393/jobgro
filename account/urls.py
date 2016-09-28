from django.conf.urls import url
import account.views

urlpatterns =[
    url(r'^student', account.views.student_register, name='student_register'),
]