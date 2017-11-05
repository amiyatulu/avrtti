"""Views of Posts."""
from django.shortcuts import render
from posts.models import Post, PostHash, PostsForm, PostHashForm, Tag, TagForm
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from posts.serializers import PostSerializer, PostHashSerializer, TagSerializer


class PostViewSet(viewsets.ModelViewSet):
    """API endpoint that allows posts to be viewed or edited."""

    queryset = Post.objects.all().order_by('-create_time')
    serializer_class = PostSerializer


class PostHashViewSet(viewsets.ModelViewSet):
    """API endpoint that allows posthash to be viewed or edited."""

    queryset = PostHash.objects.all()
    serializer_class = PostHashSerializer


class TagViewSet(viewsets.ModelViewSet):
    """API endpoint that allows tags to be viewed or edited."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


def index(request):
    """Index Views."""
    return render(request, 'posts/index.html')

def viewPosts(request, post_id):
    post = Post.object.get(pk=post_id)
    context = {'post': post}
    return render(request, 'posts/posts.html', context)



def createPosts(request):
    """Post Views."""
    if request.method == "POST":
        p_form = PostsForm(request.POST, prefix="p")
        a_form = PostHashForm(request.POST, prefix="a")
        if p_form.is_valid() and a_form.is_valid():
            p_form.save()
            a_form.save()
            return HttpResponseRedirect(reverse('posts: view_posts'))
    else:
        p_form = PostsForm(prefix="p")
        a_form = PostHashForm(prefix="a")

    return render(request, 'posts/create_posts.html',{'p_form':p_form, 'a_form':a_form})
