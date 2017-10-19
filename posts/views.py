"""Views of Posts."""
from django.shortcuts import render


def index(request):
    """Index Views."""
    return render(request, 'posts/index.html')

# Create your views here.
