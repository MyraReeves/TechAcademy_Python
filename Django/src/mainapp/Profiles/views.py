from django.shortcuts import render
from .models import Profile

# Create your views here.
def username_list(request):
    users = Profile.objects.all()
    return render(request, 'Profiles/user_login.html', {'registered_users': users})
