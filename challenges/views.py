from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def january(request):
#     return HttpResponse('january')
#
# def sunday(request):
#     return HttpResponse('sunday')
#
#
# def march(request):
#     return HttpResponse('march')
def monthly_challenges_by_number(request, month):
    return HttpResponse(month)

def monthly_challenges(request, month):
    text = '';
    if month == 'january' :
        text = 'january 1'
    elif month == 'feb':
        text = 'feb 2'
    else:
        text = 'month not found!'
    return HttpResponse(text)

