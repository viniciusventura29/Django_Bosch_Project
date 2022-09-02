from django.contrib import admin
from .models import Usuario,Text,Comentario

class UsuariosDisplay(admin.ModelAdmin):
    list_display = ('id','nome','apelido')
    
class TextDisplay(admin.ModelAdmin):
    list_display=('id','user_id','title')
    
class ComentarioDisplay(admin.ModelAdmin):
    list_display=('id','text_id')
    
admin.site.register(Usuario,UsuariosDisplay)
admin.site.register(Text,TextDisplay)
admin.site.register(Comentario,ComentarioDisplay)