from django.shortcuts import render



def index(request):
    return render(request,'index.html')

def consultaticket(request):
    return render(request,'consultaticket.html')

def consultaDeCredito(request):
    return render(request,'consultadecredito.html')