from models.models import *
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from business import accountkit
import random
import string
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    dic = {
        'FACEBOOK_APP_ID': '374722036360552',
        'csrf': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(36)),
        'ACCOUNT_KIT_API_VERSION': 'v1.1'
    }
    return render(request, 'login.html', dic)



from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def authCode(request):
    if request.method == "POST":
        user_data=json.loads(request.body)
        accountkit_data = accountkit.validate_accountkit_access_token(accountkit.get_accountkit_access_token(request.body))
        exists = AppAuthData.objects.filter(account_kit_id = accountkit_data[0]).exists() 
        if exists:
            print('exists')
            # user already exist pop up

        else:
            appAuthData = AppAuthData(
                account_kit_id = accountkit_data[0],
                phone_number = accountkit_data[1]
            )
            appAuthData.save()

            userInfo=UserInfo(app_auth_data_id=appAuthData,first_name=user_data['first_name'],\
                last_name=user_data['last_name'],email=user_data['email'],date_of_birth=user_data['dob'])
            userInfo.save()


        myResponse = HttpResponse()
        myResponse.set_cookie(key='goalstar', value=accountkit_data, max_age=31536000, httponly=True)

        return myResponse
    return HttpResponse("hi")

def notify(request):
    if request.method == "POST":
        print(request.body)
        
        notify_me = catch_email_temp(
            email=str(request.body)
        )
        notify_me.save()


        return HttpResponse('')


def registerUser(request):
    if request.method=="POST":
        print(request.POST)
        phone_number=request.POST['phone_number']
        country_code=request.POST['country_code']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        dob=request.POST['dob']
        data={}

        if AppAuthData.objects.all().filter(phone_number=country_code+phone_number):
            data={'output':"yes"}
        else:            
           data={'output':"no"}
        return JsonResponse(data)