from django.shortcuts import render
from django.http import HttpResponse

# Funcion index
def index(request):
    print('Soy un log de servidor.')
    #Print sirve para imprimir
    print('--Entrando al index--')
    return HttpResponse("soy la verga.")





