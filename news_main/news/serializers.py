from rest_framework import serializers
from .models import Article,User

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'author','title','description','url','publishedAt')
# testing this to see if I can keep similar format
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','password','first_name','last_name','date_joined')
