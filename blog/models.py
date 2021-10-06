from django.db import models

# Post - all blogs are stored in here
class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

# Contact - all sent contacts stored in here
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=150)
    message = models.TextField()
