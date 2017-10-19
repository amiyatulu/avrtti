"""Url for Post."""
from django.conf.urls import url
from posts import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
