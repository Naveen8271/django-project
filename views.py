from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from .models import student, Patient
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from .forms import PatientForm  # assuming you have this form in forms.py

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    students = student.objects.all()
    return render(request, "contact.html", {'student_list': students})

def details(request, slug):
    student_obj = get_object_or_404(student, slug=slug)
    return render(request, "details.html", {'student': student_obj})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

def patient_detail(request, slug):
    patient = get_object_or_404(Patient, slug=slug)
    return render(request, 'patients/patient_detail.html', {'patient': patient})

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')  # fixed redirect name to match urls.py
    else:
        form = PatientForm()
    return render(request, 'patients/patient_form.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # redirect to home after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('contact')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form}) 
