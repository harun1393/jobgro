from .models import Contact
from django.contrib.auth.models import User


class AccountAuthBackend(object):
    def authenticate(self,email=None):
        try:
            user = User.objects.get(email=email)
            if user:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
