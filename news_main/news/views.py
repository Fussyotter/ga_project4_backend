from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.contrib.auth import login, authenticate
=======
from django.contrib.auth import login
>>>>>>> 6dd9718 (redid model for user and swapped to default django)
from django.contrib.auth.forms import UserCreationForm
from rest_framework import generics
from .serializers import ArticleSerializer
from .models import Article
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
# Create your views here.

class UserRegistrationView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# def my_view(req):
#     username = req.POST['username']
#     password = req.POST['password']
#     user = authenticate(req,username=username,password=password)
#     if user is not None:
#         login(req,user)
#     else:
#         print('heheh')
