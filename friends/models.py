from django.db import models
from django.contrib.auth import get_user_model
# Create your dels here.
User = get_user_model()

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    follower = models.ForeignKey(User, on_delete=models.CASCADE)