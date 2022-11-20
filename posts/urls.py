from django.urls import path
from .views import PostDetail, PostList, PostCreate

urlpatterns = [
    path("", PostList, name="postlist"),
    path("create/", PostCreate.as_view(), name="postcreate"),
    path("<str:title>/", PostDetail, name="postdetail"),
]
