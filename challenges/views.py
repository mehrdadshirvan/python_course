from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound,Http404
from django.urls import reverse
from django.template.loader import render_to_string

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
    'oct': '',
    'nov': 'november',
    'dec': 'december',
}


def index(request):
    list_items = "";
    months = list(monthly_challenges_dic.keys())
    # for month in months:
    #     cap_month = month.capitalize()
    #     path = reverse('month-challenge', args=[month])
    #     list_items += f"<li><a href='{path}'>{cap_month}</a></li>"
    # res_date = f"<ul>{list_items}</ul>"
    return render(request, "challenges/index.html", {"months": months})

    # return HttpResponse(res_date)


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges_dic.keys())
    if (month - 1) > len(months):
        return HttpResponseNotFound("invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        text = monthly_challenges_dic[month]
        context = {
            "text": text,
            "name": month
        }
        return render(request, "challenges/challenge.html", context)
    except:
        raise Http404()
