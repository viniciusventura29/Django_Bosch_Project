from django.shortcuts import render, redirect
from django.core.validators import validate_email
from home.models import TextModel, UsuarioModel
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

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
            return render(request, 'escrever.html')

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
        )
    
        texto.save()
        messages.success(request,"salvo com sucesso!")   
    
    
        return render(request, "escrever.html")
    
    else:
        return render(request, "escrever.html")