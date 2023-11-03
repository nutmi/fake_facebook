from django.shortcuts import render
from .serializers import Room1to1Serializer, MessageSerializer
from .models import Room1to1, Message
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from django.db.models import Q
# Create your views here.
User =get_user_model()

class Room1to1ViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = Room1to1Serializer
    lookup_field = "id"
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Room1to1.objects.filter(Q(user_1=self.request.user) | Q(user_2=self.request.user))
    

class MessageViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = MessageSerializer
    lookup_field = "id"
    authentication_classes = [TokenAuthentication]
    queryset = Message.objects.all()