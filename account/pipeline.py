from account.models import MyUser
from student.models import StudentProfile


def associate_by_email(**kwargs):
    try:
        email = kwargs['details']['email']
        kwargs['user'] = MyUser.objects.get(email=email)
    except:
        pass
    return kwargs


def save_profile(backend, user,response, *args, **kwargs):
    if kwargs['is_new']:
        print "usr profile in if "
        profile = StudentProfile.objects.create(user=user)
        profile.name = response.get('name')
        profile.city = response.get('location')
        profile.save()
    else:
        print "user profile in else"
        pass
