from django.db import models

import swipes

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 200, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length = 200, unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    # avatar = models.ImageField(null=True, default="avatar.svg", blank=True)

class File(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length = 200, null=True, blank=True)
    owners = models.ManyToManyField(User, on_delete=models.DO_NOTHING, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length = 200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    information = models.TextField()



class Swipe(models.Model):
    name = models.CharField(max_length = 200, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    owners = models.ManyToManyField(User, on_delete=models.DO_NOTHING, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    file = models.ForeignKey(File, on_delete=models.CASCADE, null=False)
    project = models.ManyToManyField(File, on_delete=models.DO_NOTHING, null=True)
