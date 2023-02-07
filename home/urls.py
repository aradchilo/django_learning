from django.urls import path

from . import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('login', views.LoginInterfaceView.as_view(), name='Login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='Logout'),
    path('signup', views.SignupView.as_view(), name='Signup')
]