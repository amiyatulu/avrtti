"""Url for Post."""
from django.conf.urls import url, include
from posts import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet)
router.register(r'posthash', views.PostHashViewSet)
router.register(r'tag', views.TagViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^index$', views.index, name='index'),
    url(r'^posts/[0-9]/$', views.viewPosts, name="view_posts"),
    url(r'^create-posts$', views.createPosts, name="create_posts"),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'create_user', views.create_user, name="create_user"),
]
