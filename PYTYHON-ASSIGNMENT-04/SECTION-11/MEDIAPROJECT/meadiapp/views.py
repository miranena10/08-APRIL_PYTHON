from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import ProfileForm
from .models import InfluencerProfile


def edit_profile(request):

    user = User.objects.first()   # Temporary user

    profile, created = InfluencerProfile.objects.get_or_create(
        user=user
    )

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})


def profile(request):

    user = User.objects.first()   # Temporary user

    profile, created = InfluencerProfile.objects.get_or_create(
        user=user
    )

    return render(request, 'profile.html', {'profile': profile})