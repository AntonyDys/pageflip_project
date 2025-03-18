from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.template.defaultfilters import slugify


class SubGenreCategory(models.Model):#sub-genres for the books, like categories in the text book
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    # slug field - makes url pretty.
    slug = models.SlugField(unique=True, blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Sub-Genre Categories'

    def save(self, *args, **kwargs):
        # generate a slug from the name field before saving c:
        self.slug = slugify(self.name)
        super(SubGenreCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class BookPage(models.Model):#the books themselves
    TITLE_MAX_LENGTH = 128
    title = models.CharField(max_length=TITLE_MAX_LENGTH, unique=True)
    author = models.CharField(max_length=TITLE_MAX_LENGTH)
    year_of_publication = models.PositiveIntegerField()
    series_info = models.CharField(max_length=50) #Standalone or part of a Series
    description = models.TextField()  # longer than CharField if needed
    subgenres = models.ManyToManyField(SubGenreCategory)
    slug = models.SlugField(unique=True, blank=True, null=True) #making urls pretty

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BookPage, self).save(*args, **kwargs)

    def average_rating(self):
        #ratings = self.ratings.all()
        avg = self.ratings.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 1) if avg is not None else 0

    def __str__(self):
        return self.title

class UserProfile(models.Model):#for a user profile, still in progress
    #links profile to a user model provided by Django (Has all the basic stuff)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional attributes for pageflip that we wanted, profile image is set to a default one but can be changed
    profilePicture = models.ImageField(upload_to='profile_images', blank=True, default='profile_images/default-picture.png')
    userAboutMe = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class BookRating(models.Model):#model for the ratings, uses Users as a FK
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookPage, on_delete=models.CASCADE, related_name="ratings")
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1,6)])

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user.username} rated this book {self.rating} stars"

