from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=200, null=True, unique=True)


class Snippet(models.Model):

    title = models.CharField(max_length=200, null=True)
    created_user = models.ForeignKey(User, related_name="snippet", on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=500)
    tag = models.ForeignKey(Tag, related_name="snippet", on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
