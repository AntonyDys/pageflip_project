from django.urls import path
from pageflip import views

app_name = 'pageflip'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]