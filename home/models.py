from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
class TextModel(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.PROTECT)
    title = models.CharField(max_length=25)
    body = models.TextField()
    rate = models.IntegerField(default=0)
    categoria = models.CharField(max_length=25)
    data = models.DateField(auto_now_add=True)
    
class ComentarioModel(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.PROTECT)
    text_id = models.ForeignKey(TextModel,on_delete=models.PROTECT)
    body = models.CharField(max_length=120)
