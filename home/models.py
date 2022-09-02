from tkinter import CASCADE
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=25)
    apelido = models.CharField(max_length=15)
    email = models.EmailField()
    senha = models.CharField(max_length=20)
    image = models.ImageField()
    
    
class Text(models.Model):
    user_id = models.ForeignKey(Usuario,on_delete=models.PROTECT)
    title = models.CharField(max_length=25)
    body = models.TextField()
    
class Comentario(models.Model):
    user_id = models.ForeignKey(Usuario,on_delete=models.PROTECT)
    text_id = models.ForeignKey(Text,on_delete=models.PROTECT)
    body = models.CharField(max_length=120)
