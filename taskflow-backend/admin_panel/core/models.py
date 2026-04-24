from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)

class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)