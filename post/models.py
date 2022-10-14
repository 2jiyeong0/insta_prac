from django.db import models
from user.models import User

# Create your models here.
class Post(models.Model):
    class Meta:
        db_table = "post"

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)