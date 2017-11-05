from posts.models import Post, PostHash, Tag
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description', 'create_time', 'update_time', 'post_hash', 'tags')


class PostHashSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostHash
        fields = ('describe_change', 'hashcode', 'create_time', 'update_time')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'title', 'description', 'create_time', 'update_time')
