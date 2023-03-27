from django.contrib import admin
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('title', 'user')

# this was used to display many to one relationship but the below is a way to do both with less code.

# https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#inlinemodeladmin-objects

# Using @admin.register decorator for both models and defining Articleinline as a nested class.  Down the documentation rabbit hole.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
# ok .through is defining a table that connects the many to many relationship.  through is an intermediary table for many to many
class ArticleInline(admin.TabularInline):
    model = Article.user.through
    extra = 1


class CustomUserAdmin(UserAdmin):
    inlines = [ArticleInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     class ArticleInline(admin.TabularInline):
#         model = Article
#     inlines = [ArticleInline]
#     list_display = ('email',)





#############################################

#saw more dry way to do admin definition


# admin.site.register(User, UserAdmin)
# admin.site.register(Article)
#  this is how you view the one to many relationship.  The many to one relationship from Article to User is much simpler.
#
# Register your models here.
# for everything we want to see on the admin page we have to import it and bring it in.
