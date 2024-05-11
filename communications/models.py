# In communication/models.py
from django.contrib.auth.models import User
from django.db import models

class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
