
from django.db import models
from django.contrib.auth.models import User


class SmallGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class GroupMember(models.Model):
    group = models.ForeignKey(SmallGroup, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)

class Meeting(models.Model):
    group = models.ForeignKey(SmallGroup, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
