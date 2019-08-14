from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('register',views.registerUser,name='registerUser'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('auth-code', views.authCode, name='authCode'),
    path('notify', views.notify, name='notify')
]