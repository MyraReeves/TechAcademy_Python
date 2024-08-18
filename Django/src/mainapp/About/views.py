from django.shortcuts import render

# Create your views here.
def greeting(request):
    user = request.user
    context = {
        'userKey': user,
    }
    return render(request, "about.html", context)
