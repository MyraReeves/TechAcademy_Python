from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from .forms import ProfileForm


# Create your method views here.

def username_list(request):
    users = Profile.objects.all()
    return render(request, 'Profiles/user_login.html', {'registered_users': users})

# ____________________________________________________________________


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
        return render(request, 'Profiles/selected_profile.html', {'form': form})

# ____________________________________________________________________


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('username_list')
    else:
        context = {"item": item,}
        return render(request, "Profile/confirmDelete.html", context)

# ____________________________________________________________________


def confirmed(request):
    if request.method == 'POST':
        # Create form:
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('username_list')
    else:
        return redirect('username_list')
