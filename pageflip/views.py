from django.shortcuts import render
from django.http import HttpResponse

from pageflip.forms import UserForm, UserProfileForm


def index(request):

    context_dict = {}
    context_dict['boldmessage'] = 'This months genre: Sci-fi!'

    response = render(request, 'pageflip/index.html', context=context_dict)

    return response

def about(request):
    return HttpResponse("About us")

def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()


            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profilePicture' in request.FILES:
                profile.profilePicture = request.FILES['profilePicture']

            profile.save()

            registered = True
        else:

            print(user_form.errors, profile_form.errors)
    else:

        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'pageflip/register.html',context={'user_form': user_form,
                                                             'profile_form':profile_form,
                                                             'registered': registered})



def user_login(request):
    return HttpResponse("This is the login page")