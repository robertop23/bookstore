from rest_framework import serializers
from bookstore.models import Book, ConsumerBook, Author, Publisher
from djoser.serializers import UserSerializer
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class AuthorSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False)

    class Meta:
        model = Author
        fields = ('author',)


class publisherSerializer(serializers.ModelSerializer):
    publisher = UserSerializer(many=False)

    class Meta:
        model = Publisher
        fields = ('publisher',)


class BookSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='name'
    )
    author = AuthorSerializer(many=False)
    publisher = publisherSerializer(many=False)

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'publish_date',
            'summary',
            'cover',
            'category',
            'author',
            'publisher',
        )


class ConsumerBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumerBook
        fields = (
            'book',
            'status',
        )


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class CustomUserSerializer(UserSerializer):
    groups = GroupSerializer(many=True)

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ("groups",)
