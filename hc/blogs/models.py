from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    body = models.TextField(max_length=500)
    category = models.ForeignKey(Category, null=True)
    created_date = models.DateTimeField(null=True)
