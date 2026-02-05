from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Donor, BloodRequest


# 🔐 Signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # saves user with hashed password
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# 🔑 Login
def login_user(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # redirect to dashboard after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'registration/login.html')


# 🚪 Logout
def logout_user(request):
    logout(request)
    return redirect('login')


# 👥 Donors (CREATE + LIST + FILTER)
@login_required
def donors(request):
    if request.method == "POST":
        Donor.objects.create(
            user=request.user,
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            gender=request.POST.get('gender'),
            phone=request.POST.get('phone'),
            city=request.POST.get('city'),
            blood_group=request.POST.get('blood_group'),
            last_donation=request.POST.get('last_donation') or None
        )
        return redirect('donors')  # prevents duplicate submission

    bg = request.GET.get('blood_group')
    if bg:
        donor_list = Donor.objects.filter(blood_group=bg).order_by('-id')
    else:
        donor_list = Donor.objects.all().order_by('-id')

    return render(request, 'donors.html', {'donors': donor_list})


# 🏥 Blood Request
@login_required
def request_blood(request):
    if request.method == "POST":
        BloodRequest.objects.create(
            patient_name=request.POST.get('patient_name'),
            blood_group=request.POST.get('blood_group'),
            hospital=request.POST.get('hospital'),
            contact=request.POST.get('contact')
        )
        return redirect('donors')

    return render(request, 'request.html')


# 📊 Dashboard
@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {
        'donors_count': Donor.objects.count(),
        'requests_count': BloodRequest.objects.count()
    })
