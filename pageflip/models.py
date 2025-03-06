from django.db import models
from django.contrib.auth.models import User

class SubGenreCategory(models.Model):#sub-genres for the books, like categories in the text book
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Sub-Genre Categories'

    def __str__(self):
        return self.name

class BookPage(models.Model):#the books themselves
    TITLE_MAX_LENGTH = 128
    title = models.CharField(max_length=TITLE_MAX_LENGTH, unique=True)
    author = models.CharField(max_length=TITLE_MAX_LENGTH)
    genre = models.ForeignKey(SubGenreCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):#for a user profile, still in progress
    #links profile to a user model provided by Django (Has all the basic stuff)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional attributes for pageflip that we wanted
    profilePicture = models.ImageField(upload_to='profile_images', blank=True)
    userAboutMe = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
