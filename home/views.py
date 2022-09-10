from email import message
from django.shortcuts import render
from home.models import TextModel, UsuarioModel
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def escrever(request):
    if str(request.method) == 'POST':
        
        title = request.POST.get('textTitle')
        body = request.POST.get('textBody')
        categoria = request.POST.get('TextCategoria')

        texto = TextModel.objects.create(
            title = title,
            body = body,
            categoria = categoria,
        )
    
        texto.save()
        messages.success(request,"salvo com sucesso!")   
     
     
        return render(request, "escrever.html")
    
    else:
        return render(request, "escrever.html")

def cadastrar_user(request):
    return render(request,"cadastro.html")