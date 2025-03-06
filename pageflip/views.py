from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from pageflip.forms import UserForm, UserProfileForm
from pageflip.models import UserProfile


def index(request):

    context_dict = {}
    context_dict['boldmessage'] = 'This months genre: Sci-fi!'

    response = render(request, 'pageflip/index.html', context=context_dict)

    return response

def about(request):

    context_dict = {}
    context_dict ['boldmessage']= 'PageFlip is an online home for all your reading needs'

    response = render(request, 'pageflip/about.html', context=context_dict)
    return response

@login_required #this might make no sense, but its for additional things like picture and "about me"
def register_profile(request):
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect(reverse('pageflip:index'))
        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'pageflip/profile_registration.html', context_dict)

class ProfileView(View):#this is to show the user's profile properly
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        #has the about me stuff and profile picture now
        form = UserProfileForm({'aboutMe': user_profile.userAboutMe,
                                'profilePicture': user_profile.profilePicture})

        return(user, user_profile, form)

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('pageflip:index'))

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}
        return render(request, 'pageflip/profile.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('pageflip:index'))

        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save(commit=True)
            return redirect('pageflip:profile', user.username)
        else:
            print(form.errors)

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}

        return render(request, 'pageflip/profile.html', context_dict)
