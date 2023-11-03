from rest_framework import serializers
from .models import Room1to1, Message
from django.db.models import Q

class Room1to1Serializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Room1to1

    def create(self, validated_data):
        user_1 = (validated_data["user_1"])
        user_2 = (validated_data["user_2"])

        if user_1 == user_2 or Room1to1.objects.filter(Q(user_1=user_1, user_2=user_2) | Q(user_1=user_2, user_2=user_1)).exists():
            raise serializers.ValidationError
        return super().create(validated_data)

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["text", "sender", "room"]
        model = Message

    def create(self, validated_data):
        sender = validated_data["sender"]
        room_data = validated_data["room"]
        room = Room1to1.objects.get(id=room_data.id)
        if room.user_1 == sender or room.user_2 == sender:
            return super().create(validated_data)
        else:
            raise serializers.ValidationError