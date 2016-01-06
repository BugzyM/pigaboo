from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, User, check_password
from django.contrib.auth.backends import ModelBackend
from django.conf import settings

class EmailBackend(ModelBackend):

    def authenticate(self, username=None, password=None, **kwargs):
        if '@' in username:
            _kwargs = { 'email': username }

        try:
            user = User.objects.get(**_kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
