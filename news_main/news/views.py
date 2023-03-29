from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.views import View
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
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# not using the below really at all, i just left it in because it was first attempt before djoser
class UserLoginView(View):
    def post(self, req):
        username = req.POST.get('username')
        password = req.POST.get('password')

        if username is None or password is None:
            return HttpResponse(status=400)

        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)

    def delete(self, req):
        logout(req)
        return HttpResponse(status=200)
