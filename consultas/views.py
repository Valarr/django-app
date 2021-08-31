from django.shortcuts import render



def index(request):
    return render(request,'index.html')

def consultaticket(request):
    return render(request,'consultaticket.html')

def consultadecredito(request):
    return render(request,'consultadecredito.html')

def mostrarticket(request):
    data ={
        'user_name' : 'Arcelino'
    }
    return render(request,'mostrarticket.html',data)