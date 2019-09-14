from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

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
    path('detail_tournament',views.detail_tournament,name='detail_tournament'),
    path('match_in_tournament',views.match_in_tournament,name='match_in_tournament'),
	path('cancel',views.cancel,name='cancel'),
	path('checkout',views.checkout,name='checkout'),
	path('response',views.response,name='response'),
    path('change',views.change,name='change')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)