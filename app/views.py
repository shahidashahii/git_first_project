from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def shahida (request):
    return HttpResponse('shahida is a good girl')

def yasmeen (request):
    return HttpResponse('yasmeen is my sister')