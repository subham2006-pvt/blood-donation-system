from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),  # 👈 ROOT FIX

    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('donors/', views.donors, name='donors'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('request/', views.request_blood, name='request'),
]
