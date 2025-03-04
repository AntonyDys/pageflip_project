from django.db import models
from django.contrib.auth.models import User









class UserProfile(models.Model):
    #links profile to a user model provided by Django (Has all the basic stuff)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional attributes for pageflip that we wanted
    profilePicture = models.ImageField(upload_to='profile_images', blank=True)
    userAboutMe = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
