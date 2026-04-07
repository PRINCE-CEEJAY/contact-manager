from django.db import models
from django.contrib.auth.models import User


class ManagerModel(models.Model):
    name = models.CharField()
    email = models.EmailField()
    bio = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
