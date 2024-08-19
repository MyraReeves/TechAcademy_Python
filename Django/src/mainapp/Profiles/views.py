from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from .forms import ProfileForm

# Create your method views here.

def username_list(request):
    users = Profile.objects.all()
    return render(request, 'Profiles/user_login.html', {'registered_users': users})

def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Profile, pk=pk)
    form = ProfileForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('username_list')
        else:
            print(form.errors)
            
    else:
        return render(request, 'Profiles/selected_profile.html', {'form':form})
        