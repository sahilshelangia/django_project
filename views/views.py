from models.models import *
from django.shortcuts import render, HttpResponse
from business import accountkit
import random
import string
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')

def login(request):
    dic = {
        'FACEBOOK_APP_ID': '374722036360552',
        'csrf': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(36)),
        'ACCOUNT_KIT_API_VERSION': 'v1.1'
    }
    return render(request, 'login.html', dic)

def authCode(request):
    if request.method == "POST":
        accountkit_data = accountkit.validate_accountkit_access_token(accountkit.get_accountkit_access_token(request.body))

        exists = AppAuthData.objects.filter(account_kit_id = accountkit_data[0]).exists() 
        if exists:
            print('exists')
        else:
            appAuthData = AppAuthData(
                account_kit_id = accountkit_data[0],
                phone_number = accountkit_data[1]
            )
            appAuthData.save()

        myResponse = HttpResponse()
        myResponse.set_cookie(key='goalstar', value=accountkit_data, max_age=31536000, httponly=True)

        return myResponse

def notify(request):
    if request.method == "POST":
        print(request.body)
        
        notify_me = catch_email_temp(
            email=str(request.body)
        )
        notify_me.save()


        return HttpResponse('')