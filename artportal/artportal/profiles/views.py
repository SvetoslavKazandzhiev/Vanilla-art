from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from artportal.profiles.forms import ProfileForm
from artportal.profiles.models import Profile


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm(instance=profile)
    context = {
        'form': form,
    }

    return render(request, 'profiles/details.html', context)


def view_profile(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile,
    }
    return render(request, 'profiles/view-profile.html', context)