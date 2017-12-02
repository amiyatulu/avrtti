from django.db import models
from django.forms.models import ModelForm
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    description = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(
        Tag,
        related_name="tags",
        related_query_name="tag",)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PostHash(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    describe_change = models.TextField()
    hashcode = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)



class ReviewPost(models.Model):
    posts = models.OneToOneField(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ReviewHash(models.Model):
    reviewpost = models.ForeignKey(ReviewPost, on_delete=models.CASCADE)
    describe_change = models.TextField()
    hashcode = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)

class PostsForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']

class PostHashForm(ModelForm):
    class Meta:
        model = PostHash
        fields = ['describe_change']

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'title', 'description']
