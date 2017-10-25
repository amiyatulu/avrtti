"""Views of Posts."""
from django.shortcuts import render


def index(request):
    """Index Views."""
    return render(request, 'posts/index.html')


def posts(request):
    """Post Views."""
    return render(request, 'posts/posts.html')
