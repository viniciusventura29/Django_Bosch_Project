from django.contrib import admin
from .models import TextModel,ComentarioModel
    
class TextDisplay(admin.ModelAdmin):
    list_display=('id','user_id','title','body','rate','categoria','data')
    
class ComentarioDisplay(admin.ModelAdmin):
    list_display=('id','text_id')
    

admin.site.register(TextModel,TextDisplay)
admin.site.register(ComentarioModel,ComentarioDisplay)