from django.urls import path
from . import views
from .views import UserRegistrationView

urlpatterns = [
 
    # path('login', my_view.as_view(), name='login' ),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('articles', views.ArticleList.as_view(), name='article_list'),
    path('articles/<int:pk>', views.ArticleDetail.as_view(), name='articles_detail'),
]
