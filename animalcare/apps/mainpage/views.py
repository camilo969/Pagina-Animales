from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def america(request):
    return render(request,'america.html')

def europa(request):
    return render(request,'europa.html')

def asia(request):
    return render(request,'asia.html')

def oceania(request):
    return render(request,'oceania.html')

def africa(request):
    return render(request,'africa.html')

def donaciones(request):
    return render(request,'donaciones.html')