from statistics import mode
from tkinter import CASCADE
from django.db import models

class UsuarioModel(models.Model):
    nome = models.CharField(max_length=25)
    apelido = models.CharField(max_length=15)
    email = models.EmailField()
    senha = models.CharField(max_length=20)
    image = models.ImageField()
    
    
class TextModel(models.Model):
    user_id = models.ForeignKey(UsuarioModel,on_delete=models.PROTECT)
    title = models.CharField(max_length=25)
    body = models.TextField()
    rate = models.IntegerField()
    categoria = models.CharField(max_length=25)
    
    
class ComentarioModel(models.Model):
    user_id = models.ForeignKey(UsuarioModel,on_delete=models.PROTECT)
    text_id = models.ForeignKey(TextModel,on_delete=models.PROTECT)
    body = models.CharField(max_length=120)
