from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    firstname = models.CharField(max_length=30, blank=False, null=False)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=7, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return self.firstname

		
class ProfileInvites(models.Model):		
    profile = models.ManyToManyField(UserProfile)
    invitee = models.ManyToManyField(User)
    status = models.CharField(max_length=20, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

class ProfileFiles(models.Model):		
    profile = models.ManyToManyField(UserProfile)
    locked = models.ManyToManyField(User, blank=True, null=True)
    filename = models.CharField(max_length=256, blank=False, null=False)
    fullpath = models.CharField(max_length=10240, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
	
class ChatMessage(models.Model):
    user = models.ForeignKey(UserProfile)
    chatroom = models.CharField(max_length=30, blank=False, null=True)
    message = models.CharField(max_length=1024, blank=False, null=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
   
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
