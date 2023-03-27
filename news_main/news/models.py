from django.db import models
from django.contrib.auth.models import User



# this is basic model for the v2/everything end point.
# probably need more models to get more specific but this is a start

# basic template i'm testing


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email


class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=120)
    url = models.CharField(max_length=120)
    publishedAt = models.CharField(max_length=50)
    user = models.ManyToManyField(User)
    def __str__(self): return self.title

    # This column needed to be clean
    # trying one to many relationship
    # needs a default, kept getting errors
    # user has to be declared first if i'm using a custom one.
# Create your models here.


# this is basic model for the v2/everything end point.
# probably need more models to get more specific but this is a start

# basic template i'm testing


# class User(models.Model):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=120)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     date_joined = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.email
