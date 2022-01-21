from django.db import models

# Create your models here.
class Message(models.Model):
    user = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    status = models.CharField(max_length=100)
