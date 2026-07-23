from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile

@login_required(login_url='/accounts/login/')
def profile_view(request):
    # Get or create profile for the user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone_number = request.POST.get("phone_number", "").strip()
        delivery_address = request.POST.get("delivery_address", "").strip()
        
        # Sync with auth User email
        if email:
            request.user.email = email
            request.user.save()
            
        profile.name = name
        profile.phone_number = phone_number
        profile.delivery_address = delivery_address
        
        # Handle file upload
        if request.FILES.get("profile_picture"):
            profile.profile_picture = request.FILES.get("profile_picture")
            
        profile.save()
        messages.success(request, "Your profile has been updated successfully.")
        return redirect('profile')
        
    return render(request, "profile.html", {"profile": profile})
