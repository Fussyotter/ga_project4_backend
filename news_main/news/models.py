from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=120)
    url = models.CharField(max_length=120)
    publishedAt = models.CharField(max_length=50)
    def __str__(self): return self.name

# this is basic model for the v2/everything end point.  
# probably need more models to get more specific but this is a start