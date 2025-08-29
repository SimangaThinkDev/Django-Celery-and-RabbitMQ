from django.shortcuts import render, HttpResponse
from .tasks import add

# Create your views here.



def my_view(request):
    result = add.delay(4, 4)
    return HttpResponse('Task started')