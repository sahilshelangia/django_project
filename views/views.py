from models.models import *
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from business import accountkit
from business.models import *
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




def authCode(request):
    if request.method == "POST":
        accountkit_data = accountkit.validate_accountkit_access_token(accountkit.get_accountkit_access_token(request.POST['accountkit_data']))
        # appAuthData = AppAuthData(
        #         account_kit_id = accountkit_data[0],
        #         phone_number = accountkit_data[1]
        #     )
        # appAuthData.save()

        # # create profile for the same
        # userInfo=UserInfo(app_auth_data_id=appAuthData,first_name=request.POST['first_name'],\
        #     last_name=request.POST['last_name'],email=request.POST['email'],date_of_birth=request.POST['dob'],\
        #     subscription_type_id=SubscriptionType.objects.get(subscription="free"),expiry_date=datetime.date.today()+datetime.timedelta(days=90))
        # userInfo.save()

        userInfoModel=UserInfoModel()
        userInfoModel.account_kit_id=accountkit_data[0]
        userInfoModel.phone_number=accountkit_data[1]
        userInfoModel.first_name=request.POST['first_name']
        userInfoModel.last_name=request.POST['last_name']
        userInfoModel.email=request.POST['email']
        userInfoModel.date_of_birth=request.POST['dob']
        userInfoModel.subscription_type_id=SubscriptionType.objects.get(subscription="free")
        userInfoModel.expiry_date=datetime.date.today()+datetime.timedelta(days=90)
        userInfoModel.save()
        # add notification to the same
        for obj in NotificationType.objects.all():
            userNotificationType=UserNotificationType(app_auth_data=appAuthData,notification_type_id=obj)
            userNotificationType.save()

        myResponse = render(request,'home.html',{})
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