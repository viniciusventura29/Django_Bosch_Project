from django.contrib import admin
from .models import UsuarioModel,TextModel,ComentarioModel

class UsuariosDisplay(admin.ModelAdmin):
    list_display = ('id','nome','apelido')
    
class TextDisplay(admin.ModelAdmin):
    list_display=('id','user_id','title','body','rate','categoria')
    
class ComentarioDisplay(admin.ModelAdmin):
    list_display=('id','text_id')
    
admin.site.register(UsuarioModel,UsuariosDisplay)
admin.site.register(TextModel,TextDisplay)
admin.site.register(ComentarioModel,ComentarioDisplay)