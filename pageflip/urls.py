from django.urls import path
from pageflip import views

app_name = 'pageflip'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('books/', views.books, name='books'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('profile/<username>/edit_profile', views.EditProfileView.as_view(), name='edit_profile'),
]