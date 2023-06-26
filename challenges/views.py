from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

monthly_challenges_dic = {
    'jan': 'january',
    'feb': 'february',
    'mar': 'march',
    'apr': 'april',
    'may': 'may',
    'jun': 'june',
    'jul': 'july',
    'aug': 'august',
    'sep': 'september',
    'oct': 'october',
    'nov': 'november',
    'dec': 'december',
}

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges_dic.keys())
    if (month-1) > len(months):
        return HttpResponseNotFound("invalid month")

    redirect_month = months[month-1]
    return HttpResponseRedirect('/challenges/'+redirect_month)

def monthly_challenges(request, month):
    try:
        text = monthly_challenges_dic[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("page not found")


