from django.contrib.auth.models import User
from .models import Article
from rest_framework import serializers
from rest_framework.request import Request


class UserSerializer(serializers.HyperlinkedModelSerializer):
    “”” Serializer de usuarios con articulos relacionados y 
    password como campo para escritura
    “””
    articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'first_name', 'last_name', 'email', 'articles')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.StringRelatedField()
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Article
        fields = ('title', 'content', 'author', 'owner', 'created', 'modified')

    def create(self, validated_data):
        author = validated_data['owner']
        validated_data.pop('owner')
        return Article.objects.create(author=author, **validated_data)
