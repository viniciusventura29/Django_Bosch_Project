from django.shortcuts import render, redirect, get_object_or_404
from django.core.validators import validate_email
from home.models import TextModel
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.http import HttpResponse

def index(request):
    textos = TextModel.objects.all()

    dados = {
        'textos':textos,
    }

    return render(request, "index.html",dados)

def cadastrar_user(request):
    if str(request.method) == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        nickname = request.POST.get('Nickname')
        first_password = request.POST.get('First_password')
        second_password = request.POST.get('Second_password')

    try:
        validate_email(email)

    except:
        messages.error(request, 'Email Inválido')
        return render(request, 'cadastro.html')

    if len(first_password)<6:
        messages.error(request, 'Senha deve ter no mínimo 6 digitos')
        return render(request, 'cadastro.html')

    if second_password!=first_password:
        messages.error(request, 'Senhas diferentes! Tente novamente')
        return render(request, 'cadastro.html')

    if User.objects.filter(username=nickname).exists():
        messages.error(request, 'Nome de usuário ja cadastrado! Tente novamente')
        return render(request, 'cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email ja cadastrado! Tente novamente')
        return render(request, 'cadastro.html')
    
    

    novo_usuario = User.objects.create_user(
        username=nickname,
        first_name=name,
        email=email,
        password=first_password
        )
    
    novo_usuario.is_staff = True
    
    novo_usuario.save()

    return render(request,"cadastro.html")

def logar_user(request):
    if str(request.method) != 'POST':
        return render(request, 'login.html')

    else:
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user_login = auth.authenticate(
            username=username,
            password=senha,
        )

        if user_login:
            auth.login(request,user_login)
            return redirect('escrever')

        else:
            messages.warning(request,"Usuário não cadastrado!")
            return render(request, 'login.html')
        
def sair_user(request):
    auth.logout(request)
    return redirect('index')
        

def escrever(request):
    if str(request.method) == 'POST':
        title = request.POST.get('textTitle')
        body = request.POST.get('textBody')
        categoria = request.POST.get('TextCategoria')

        texto = TextModel.objects.create(
            title = title,
            body = body,
            categoria = categoria,
            user_id = request.user,
        )
    
        texto.save()
        messages.success(request,"salvo com sucesso!")   
    
    
        return render(request, "escrever.html")
    
    else:
        return render(request, "escrever.html")
    
def texto(request,texto_id):
    texto = get_object_or_404(TextModel, pk=texto_id)
    texto_a_ser_exibido = {
        'texto':texto,
    }
    return render(request, "texto.html",texto_a_ser_exibido)