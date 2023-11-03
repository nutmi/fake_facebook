from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user}'s post"
