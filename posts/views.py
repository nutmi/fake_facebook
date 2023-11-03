from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth import get_user_model
from friends.models import Follower
from rest_framework.authentication import TokenAuthentication
# Create your views here.
User = get_user_model()
class PostViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = PostSerializer
    lookup_field = "id"
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        for i in Follower.objects.filter(follower=user):
            return Post.objects.filter(user=i.user)

    

