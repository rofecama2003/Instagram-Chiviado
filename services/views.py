from django.http import HttpResponse
from django.shortcuts import render

#Models
from django.contrib.auth.models import User
from services.models import MyUser

# Funcion index
def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def register(request):
    if request.methood == 'POST':
        post_from_data = request.POST
        data = dict(
            username=post_from_data.get('username'),
            email=post_from_data.get('email'),
            first_name=post_from_data.get('name'),
            password=post_from_data.get8('password'),
        )
        user = User.object.create_user(**data)
        my_user = MyUser.objects.create(user_django=user)
        print(my_user)
        return render(request, "home.html")
    return redirect('index')

def validate_user(request):
    print(request)
    return HttpResponse("Hola")
    



