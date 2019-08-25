from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('register',views.registerUser,name='registerUser'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('auth-code', views.authCode, name='authCode'),
    path('notify', views.notify, name='notify'),
    path('updateName', views.updateName, name='updateName'),
    path('updateEmail', views.updateEmail, name='updateEmail'),
    path('updatePhone', views.updatePhone, name='updatePhone'),
    path('email-verify',views.emailVerification,name='emailVerification'),
    path('activate/<token>/<account_kit_id>/',views.activate,name='activate'),
    path('phoneExist',views.phoneExist,name='phoneExist'),
    path('emailExist',views.emailExist,name='emailExist'),
]