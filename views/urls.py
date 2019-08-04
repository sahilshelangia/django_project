from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('auth-code', views.authCode, name='authCode'),
    path('notify', views.notify, name='notify'),
    path('register', views.registerUser, name='registerUser'),
]