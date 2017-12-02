from posts.models import Post, PostHash, Tag
from rest_framework import serializers
from posts.models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserASerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ('title', 'description', 'create_time', 'update_time', 'post_hash', 'tags')
        fields = "__all__"


class PostHashSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostHash
        # fields = ('describe_change', 'hashcode', 'create_time', 'update_time')
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        # fields = ('name', 'title', 'description', 'create_time', 'update_time')
        fields = '__all__'
