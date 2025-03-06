from django.contrib import admin
from pageflip.models import UserProfile, SubGenreCategory, BookPage

#categories would go here too

admin.site.register(UserProfile)
admin.site.register(SubGenreCategory)
admin.site.register(BookPage)
