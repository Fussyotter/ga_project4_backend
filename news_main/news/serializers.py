from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'author','title','description','url','publishedAt')