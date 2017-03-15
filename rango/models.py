
from django.contrib.auth.models import User
from django.db import models
from django_elasticsearch.models import EsIndexable

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    slug = models.SlugField(max_length=50,blank=True)



    def __str__(self):
        return self.name

class Page(EsIndexable,models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank = True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username