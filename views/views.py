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

        userInfoEntity=UserInfoEntity()
        userInfoEntity.app_auth_data_id=idd
        userInfoEntity.first_name=request.POST['first_name']
        userInfoEntity.last_name=request.POST['last_name']
        userInfoEntity.email=request.POST['email']
        userInfoEntity.date_of_birth=request.POST['dob']
        userInfoEntity.subscription_type_id=SubscriptionType.objects.get(subscription="free")
        userInfoEntity.expiry_date=datetime.date.today()+datetime.timedelta(days=90)
        userInfoModel=UserInfoModel()
        ins = userInfoModel.save(userInfoEntity)

        # add notification to the same
        notificationTypeModel = NotificationTypeModel()
        for obj in notificationTypeModel.get_all():
            userNotificationType=UserNotificationType(app_auth_data=idd,notification_type_id=obj)
            userNotificationType.save()

        userLog=UserLog()
        userLog.user_id = ins
        userLog.action='Registration done'
        if request.user_agent.is_mobile:
            userLog.device_name='mobile'

        if request.user_agent.is_tablet :
            userLog.device_name='tablet'
        
        if request.user_agent.is_pc:
            userLog.device_name='pc'
        userLog.save()

        myResponse = render(request,'home.html',{})
        # phone number,device Info
        myResponse.set_cookie('key','goalstar')
        myResponse.set_cookie('value',accountkit_data)
        myResponse.set_cookie('max_age',31536000, 'httponly',True)
        myResponse.set_cookie('phone',accountkit_data[1])
        myResponse.set_cookie('device',userLog.device_name)
        
        return myResponse

def notify(request):
    if request.method == "POST":
        print(request.body)
        
        notify_me = catch_email_temp(
            email=str(request.body)
        )
        notify_me.save()


        return HttpResponse('')