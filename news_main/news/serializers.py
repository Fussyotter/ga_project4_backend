from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(many=True)

    class Meta:
        model = Article
        fields = '__all__'


# testing this to see if I can keep similar format
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password','first_name','last_name')
