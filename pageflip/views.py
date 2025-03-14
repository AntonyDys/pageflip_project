from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.core.paginator import Paginator

from pageflip.forms import UserForm, UserProfileForm
from pageflip.models import UserProfile, BookPage, SubGenreCategory


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

def book_detail(request, book_id):
    book = get_object_or_404(BookPage, id=book_id)
    return render(request, "pageflip/book_detail.html", {"book": book})

def books(request):#books!
    subgenres = SubGenreCategory.objects.all()  #gets all subgenres for the sidebar (more asthetic)

    #gets the selected subgenre from the URL when selected
    selected_subgenre = request.GET.get("subgenre", None)

    if selected_subgenre:
        #filter books to show only those selected in the subgenre
        books = BookPage.objects.filter(subgenres__name=selected_subgenre).order_by("id")
    else:
        books = BookPage.objects.all().order_by("id") # all books if no subgenre is selected

    #Paginate books (15 per page) <- pretty cool
    paginator = Paginator(books, 15)
    page = request.GET.get("page")
    paged_books = paginator.get_page(page)

    context_dict = {
        "books": paged_books,
        "subgenres": subgenres,
        "selected_subgenre": selected_subgenre,  #pass the selected subgenre to the template
    }
    return render(request, "pageflip/books.html", context=context_dict)

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

#this class is for editing the profile separately from viewing it since I had trouble with displaying it and editing
#it would basically only show the profile picture and about me would just be a blank text box no matter what
class EditProfileView(View):
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
        return render(request, 'pageflip/profile_edit.html', context_dict)

    @method_decorator(login_required())
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

        return render(request, 'pageflip/profile_edit.html', context_dict)