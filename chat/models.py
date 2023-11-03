from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Room1to1(models.Model):
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_1")
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_2")

    def __str__(self) -> str:
        return f"{self.user_1} and {self.user_2} {self.id}"
    
class Message(models.Model):
    room = models.ForeignKey(Room1to1, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} in Room {self.room}"