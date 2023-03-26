from django.contrib import admin
from .models import Article, User
admin.site.register(Article)
admin.site.register(User)
# Register your models here.
# for everything we want to see on the admin page we have to import it and bring it in.
