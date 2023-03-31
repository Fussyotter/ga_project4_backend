from django.urls import path
from django.conf.urls import include
from . import views
from .views import UserRegistrationView, UserLoginView

urlpatterns = [

    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.authtoken')),
    path('login/', UserLoginView.as_view(), name='login' ),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('articles', views.ArticleList.as_view(), name='article_list'),
    path('articles/<int:pk>', views.ArticleDetail.as_view(), name='articles_detail'),
    path('articles/user/<str:username>/',
         ArticlesByUserView.as_view(), name='articles-by-user')

]
