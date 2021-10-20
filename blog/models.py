from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Post - all blogs are stored in here
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()

# Contact - all sent contacts stored in here
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=150)
    message = models.TextField()
