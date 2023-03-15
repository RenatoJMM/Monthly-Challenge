from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january": "Eat more meat for the entire month!",
    "febuary": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 3 hours at day!! ",
    "april": "Study MongoDB for at least 1 hours at day!",
    "may": "Focus on finishing your TCC! ",
    "june": "Walk for at least 30 minutes every day!",
    "july": "Practice your english in online classes!",
    "august": "Get awesome at Django creating cool Websites! ",
    "september": "Go to the gym everyday!",
    "october": "Eat better!",
    "november": "Walk for at least 40 minutes every day!",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    forward_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[
                            forward_month])  # /challenge/january

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
        #response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
