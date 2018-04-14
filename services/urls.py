from django.urls import path
from services.views import index

urlpatterns = [
    path('', index, name='index'),
]
