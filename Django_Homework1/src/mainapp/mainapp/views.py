from django.http import HttpResponse
from django.shortcuts import render
from Profiles import views


def home(request):
    user = request.user
    youtubeComedians = ["Julie Nolke", "Ryan George", "Steven He", "Fire Department Chronicles"]
    context = {
        'userKey': user,
        'comedians': youtubeComedians,
    }
    return render(request, "home.html", context)
