from django import forms
from django.contrib.auth.models import User

from pageflip.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):#this will be for the profile later

    class Meta:
        model = UserProfile
        fields = ('profilePicture', 'userAboutMe',)