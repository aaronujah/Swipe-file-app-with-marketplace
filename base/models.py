from django.db import models

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
    public = models.BooleanField(default=False)
    category = models.CharField(max_length=200)

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length = 200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Swipe(models.Model):
    name = models.CharField(max_length = 200, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    owners = models.ManyToManyField(User, on_delete=models.DO_NOTHING, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    file = models.ForeignKey(File, on_delete=models.CASCADE, null=False)
    project = models.ManyToManyField(Project, on_delete=models.DO_NOTHING, null=True)
    
class Input(models.Model):
    link = models.URLField(max_length=200, null=True)
    image = models.ImageField(null=True, default="avatar.svg", blank=True)
    text = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, null=True)
    swipe = models.ForeignKey(Swipe, on_delete=models.CASCADE, null=True)