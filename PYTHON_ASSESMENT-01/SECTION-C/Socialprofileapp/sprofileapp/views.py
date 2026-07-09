from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileForm
import csv


def create_profile(request):

    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("profile_list")

    else:
        form = ProfileForm()

    return render(request, "create_profile.html", {"form": form})


def profile_list(request):

    profiles = Profile.objects.all()

    return render(request, "profile_list.html", {"profiles": profiles})


def export_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="profiles.csv"'

    writer = csv.writer(response)

    writer.writerow(["Username", "Age", "Email", "Public"])

    profiles = Profile.objects.all()

    for profile in profiles:
        writer.writerow([
            profile.username,
            profile.age,
            profile.email,
            profile.is_public
        ])

    return response
