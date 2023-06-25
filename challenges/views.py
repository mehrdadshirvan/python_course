from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def january(request):
    return HttpResponse('january')

def sunday(request):
    return HttpResponse('sunday')