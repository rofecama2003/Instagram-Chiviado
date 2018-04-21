from django.shortcuts import render
from django.http import HttpResponse

# Funcion index
def index(request):
    return render (request, "index.html")
    



