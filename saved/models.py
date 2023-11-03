from django.db import models

# Create your models here.
class Saved(models.Model):
    user = models.TextField()
    text = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user}'s post"