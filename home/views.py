from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def escrever(request):
    return render(request, "escrever.html")