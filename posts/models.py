from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    post_hash = models.ForeignKey(PostHash, on_delete=models.CASCADE)


class PostHash(models.Model):
    describe_change = models.TextField()
    hashcode = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)

class ReviewPosts(models.Model):
    posts = models.OneToOneField(Posts, one_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    review_hash = models.ForeignKey(ReviewHash, on_delete=models.CASCADE)

class ReviewHash(models.Model):
    describe_change = models.TextField()
    hashcode = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
