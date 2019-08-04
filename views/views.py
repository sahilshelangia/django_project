from models.models import *
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from business import accountkit
import random
import string
import requests
import datetime

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
        appAuthData = AppAuthData(
                account_kit_id = accountkit_data[0],
                phone_number = accountkit_data[1]
            )
        appAuthData.save()
        # create profile for the same
        userInfo=UserInfo(app_auth_data_id=appAuthData,first_name=user_data['first_name'],\
            last_name=user_data['last_name'],email=user_data['email'],date_of_birth=user_data['dob'],\
            subscription_type_id=SubscriptionType.objects.get(subscription="free"),expiry_date=datetime.date.today()+datetime.timedelta(days=90))

        # add notification to the same
        
        userInfo.save()
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


# check user is already registered or not
def registerUser(request):
    if request.method=="POST":
        phone_number=request.POST['phone_number']
        country_code=request.POST['country_code']
        data={}
        if AppAuthData.objects.all().filter(phone_number=country_code+phone_number):
            data={'output':"yes"}
        else:            
           data={'output':"no"}
        return JsonResponse(data)

def home(request):
    return render(request,'home.html',{})        