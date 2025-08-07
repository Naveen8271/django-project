from django.urls import path
from django.http import HttpResponse
from . import views  # your existing views

# Placeholder views for missing pages
def profile_view(request):
    return HttpResponse("This is the Profile page placeholder.")

def settings_view(request):
    return HttpResponse("This is the Settings page placeholder.")

def terms_view(request):
    return HttpResponse("This is the Terms and Conditions page placeholder.")

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('details/<slug:slug>/', views.details, name='details'),

    # Patient related URLs
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/create/', views.patient_create, name='patient_create'),
    path('patients/<slug:slug>/', views.patient_detail, name='patient_detail'),

    # Auth URLs
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # make sure you have this view in views.py
    path('logout/', views.logout_view, name='logout'),  # your logout view

    # Placeholder URLs for dropdown menu items
    path('profile/', profile_view, name='profile'),
    path('settings/', settings_view, name='settings'),
    path('terms/', terms_view, name='terms'),
]
