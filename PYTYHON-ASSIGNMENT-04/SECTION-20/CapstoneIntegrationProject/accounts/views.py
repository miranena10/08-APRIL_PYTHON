from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import OTP
import random

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")
        
        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return render(request, "register.html")
            
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "register.html")
            
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "register.html")
            
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, "register.html")
            
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')
        
    return render(request, "register.html")

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        
        user = authenticate(username=username, password=password)
        if user is not None:
            # Generate OTP
            otp_code = str(random.randint(100000, 999999))
            
            # Store in DB
            OTP.objects.create(user=username, otp=otp_code)
            
            # Save username in session temporarily
            request.session["pre_otp_username"] = username
            request.session["otp_generated_at"] = timezone.now().isoformat()
            
            messages.info(request, "OTP has been generated. Please verify.")
            return redirect("verify")
        else:
            messages.error(request, "Invalid username or password.")
            
    return render(request, "login.html")

def verify(request):
    username = request.session.get("pre_otp_username")
    if not username:
        messages.error(request, "Please log in first.")
        return redirect("login")
        
    # Get last OTP generated for this user
    last_otp = OTP.objects.filter(user=username).last()
    
    if request.method == "POST":
        entered_otp = request.POST.get("otp", "").strip()
        
        if not last_otp:
            messages.error(request, "No OTP found. Please try logging in again.")
            return redirect("login")
            
        # Check Expiration (3 minutes)
        now = timezone.now()
        elapsed_time = now - last_otp.created
        
        if elapsed_time > timedelta(minutes=3):
            messages.error(request, "OTP has expired (exceeded 3 minutes). Please log in again to receive a new one.")
            return redirect("login")
            
        if last_otp.otp == entered_otp:
            # Log the user in
            user = User.objects.get(username=username)
            auth_login(request, user)
            
            # Clean session
            if "pre_otp_username" in request.session:
                del request.session["pre_otp_username"]
            if "otp_generated_at" in request.session:
                del request.session["otp_generated_at"]
                
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("dashboard")
        else:
            messages.error(request, "Incorrect OTP code. Please try again.")
            
    return render(request, "verify.html", {
        "debug_otp": last_otp.otp if last_otp else None,
        "created_time": last_otp.created.isoformat() if last_otp else None
    })

def logout_view(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

@login_required(login_url='login')
def dashboard(request):
    # Mock movie dashboard
    movies = [
        {"title": "Inception: Re-release", "genre": "Sci-Fi / Action", "duration": "148 mins", "rating": "8.8", "image": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=400&auto=format&fit=crop&q=60"},
        {"title": "The Dark Knight", "genre": "Action / Drama", "duration": "152 mins", "rating": "9.0", "image": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=400&auto=format&fit=crop&q=60"},
        {"title": "Interstellar", "genre": "Sci-Fi / Adventure", "duration": "169 mins", "rating": "8.7", "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400&auto=format&fit=crop&q=60"}
    ]
    return render(request, "dashboard.html", {"movies": movies})