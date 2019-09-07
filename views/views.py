from models.models import *
from .basic_functionality import *
from business.accountkit import *
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse,redirect
from business import accountkit
from business.models import *
from business.entities import *
import random
import string
import requests
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.core import serializers
from django.forms.models import model_to_dict

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    if request.COOKIES.get('goalstar'):
        phone_number=findPhoneNumber(request)
        appAuthData=AppAuthDataModel.getObject('phone_number',phone_number)
        userInfo=UserInfoModel.getObject('app_auth_data_id',appAuthData) 
        trn= tournament.objects.all()
        context={'userInfo':userInfo,
                 'trn':trn,
                'FACEBOOK_APP_ID': '374722036360552',
                'csrf': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(36)),
                'ACCOUNT_KIT_API_VERSION': 'v1.1'}
        myResponse = render(request,'home.html',context=context)
        return myResponse 
    else:
        return redirect('login')
        

# logout using delete cookies
def logout(request):
    # first check user is already logged in or not
    if request.COOKIES.get('goalstar'):
        phone_number=findPhoneNumber(request)
        appAuthData=AppAuthDataModel.getObject('phone_number',phone_number)
        userInfo=UserInfoModel.getObject('app_auth_data_id',appAuthData)
       
        # log the user action
        userLog=UserLog()
        userLog.user_id=userInfo
        userLog.action='logout'
        userLog.device_name=findDevice(request)
        userLog.save()

        myResponse = redirect('login')
        myResponse.delete_cookie('goalstar')
        return myResponse
    

def login(request):
    # We have three cases for login
    # This is when user submit login form and trying to login we will use this one
    if request.POST:
        accountkit_data = accountkit.validate_accountkit_access_token(accountkit.get_accountkit_access_token(request.POST.get('login_accountkit_data')))
        device=findDevice(request)

        appAuthData=AppAuthDataModel.getObject('phone_number',accountkit_data[1])
        userInfo=UserInfoModel.getObject('app_auth_data_id',appAuthData)

        # log the user action
        userLog=UserLog()
        userLog.user_id=userInfo
        userLog.action='login'
        userLog.device_name=findDevice(request)
        userLog.save()

        myResponse = redirect('home')
        cookieInfo={'accountkit_data':accountkit_data,'device':device}
        myResponse.set_cookie(key='goalstar',value=cookieInfo,httponly=True,max_age=31536000)
        return myResponse

    # If user is already login and try to login again
    else:
        if request.COOKIES.get('goalstar'):
            return redirect('home')

        else:
            # get_facebook_app_id i will change
            dic = {
                'FACEBOOK_APP_ID': '374722036360552',
                'csrf': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(36)),
                'ACCOUNT_KIT_API_VERSION': 'v1.1'
            }
            return render(request, 'login.html', dic)



# After Checking user is already regitered or not
# call this view to register new user
def authCode(request):
    if request.method == "POST":
        accountkit_data = accountkit.validate_accountkit_access_token(accountkit.get_accountkit_access_token(request.POST['accountkit_data']))
        
        # Create AppAuthData Object Using Buisness Logic
        appAuthDataEntity=AppAuthDataEntity()
        appAuthDataEntity.account_kit_id=accountkit_data[0]
        appAuthDataEntity.phone_number=accountkit_data[1]

        appAuthDataModel=AppAuthDataModel()
        idd = appAuthDataModel.save(appAuthDataEntity)

        # create profile for the same
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

        # By Default we are going to link all type of notification for new user
        notificationTypeModel = NotificationTypeModel()
        for obj in notificationTypeModel.get_all():
            userNotificationTypeEntity = UserNotificationTypeEntity()
            userNotificationTypeEntity.app_auth_data = idd
            userNotificationTypeEntity.notification_type_id = obj
            userNotificationTypeModel = UserNotificationTypeModel()
            userNotificationTypeModel.save(userNotificationTypeEntity)

        # Save this action in user log table
        userLog=UserLog()
        userLog.user_id = ins
        userLog.action = 'registration'
        userLog.device_name=findDevice(request)
        userLog.save()

        myResponse = redirect('home')
        cookieInfo={'accountkit_data':accountkit_data,'device':userLog.device_name}
        myResponse.set_cookie(key='goalstar',value=cookieInfo,httponly=True,max_age=31536000)
        return myResponse

    dic = {
        'FACEBOOK_APP_ID': '374722036360552',
        'csrf': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(36)),
        'ACCOUNT_KIT_API_VERSION': 'v1.1'
    }
    return render(request, 'login.html', dic)


def notify(request):
    if request.method == "POST":
        print(request.body)
        
        notify_me = catch_email_temp(
            email=str(request.body)
        )
        notify_me.save()


# check user is already registered or not using AJAX
def registerUser(request):
    if request.method=="POST":
        phone_number=request.POST['phone_number']
        country_code=request.POST['country_code']
        email=request.POST['email']

        data={}
        Phone=False
        Email=False
        if AppAuthDataModel.getObject('phone_number',country_code+phone_number):
            Phone=True
        if UserInfoModel.getObject('email',email):
            Email=True
        if Phone==True and Email==True:
            data={'phone':'yes','email':'yes'}
        
        if Phone==False and Email==True:
            data={'phone':'no','email':'yes'}

        if Phone==True and Email==False:
            data={'phone':'yes','email':'no'}

        if Phone==False and Email==False:
            data={'phone':'no','email':'no'}
        return JsonResponse(data)


def updateEmail(request):
    if request.method=="POST":
        if request.COOKIES.get('goalstar'):
            phone_number=findPhoneNumber(request)
            appAuthData=AppAuthDataModel.getObject('phone_number',phone_number)
            userInfo=UserInfoModel.getObject('app_auth_data_id',appAuthData)
    
            userInfo.email=request.POST['email']
            userInfo.email_verified=False
            userInfo.save()
            data={'output':"successful"}
            return JsonResponse(data)
        else:
            return HttpResponse("Permission Denied!!!")



def emailVerification(request):
    if request.COOKIES.get('goalstar'):
        phone_number=findPhoneNumber(request)
        appAuthData=AppAuthDataModel.getObject('phone_number',phone_number)
        userInfo=UserInfoModel.getObject('app_auth_data_id',appAuthData)

        userInfo.email_token=get_random_string(length=32)
        userInfo.token_expiry=timezone.now()+timezone.timedelta(hours=1)
        userInfo.save()

        current_site = get_current_site(request)
        mail_subject = 'Activate your  account.'
        message = 'Hi,Please click on the link to confirm your email address, http://'+str(current_site.domain)\
                    +"/activate/"+userInfo.email_token+"/"+appAuthData.account_kit_id+"/"
        to_email = userInfo.email
        email = EmailMessage(
        mail_subject, message, to=[to_email]
        )
        email.send()
        data={'output':"Please confirm your email address to complete the registration"}
        return JsonResponse(data)


def activate(request, token,account_kit_id):
    appAuthData=AppAuthDataModel.getObject('account_kit_id',account_kit_id)
    userInfo=UserInfoModel.getObject('app_auth_data_id',appAuthData)
    if appAuthData and userInfo:
        if userInfo.email_token==token and userInfo.token_expiry>=timezone.now():
            userInfo.email_verified=True
            userInfo.save()
            return render(request,'email_verified.html',{})
        else: 
                return render(request,'email_not_verified.html',{})
    else:
        return render(request,'email_not_verified.html',{})



def updatePhone(request):
    if request.method == "POST":
        if request.COOKIES.get('goalstar'):
            phone_number=findPhoneNumber(request)
            appAuthData=AppAuthDataModel.getObject('phone_number',phone_number)
            res=delete_accountkit_user(appAuthData.account_kit_id)

            # save new accountkit_id and phone number as well
            accountkit_data = accountkit.validate_accountkit_access_token(accountkit.get_accountkit_access_token(request.POST['accountkit_data']))
            appAuthData.account_kit_id=accountkit_data[0]
            appAuthData.phone_number=accountkit_data[1]
            appAuthData.save()
            userInfo=UserInfoModel.getObject('app_auth_data_id',appAuthData)


            userLog=UserLog()
            userLog.user_id = userInfo
            userLog.action = 'update phone number'
            userLog.device_name=findDevice(request)
            userLog.save()

            data={'output':"yes"}
            myResponse=JsonResponse(data)
            cookieInfo={'accountkit_data':accountkit_data,'device':userLog.device_name}
            myResponse.set_cookie(key='goalstar',value=cookieInfo,httponly=True,max_age=31536000)
            return myResponse

def updateName(request):
    if request.method == "POST":
        if request.COOKIES.get('goalstar'):
            phone_number=findPhoneNumber(request)
            appAuthData=AppAuthDataModel.getObject('phone_number',phone_number)
            userInfo=UserInfoModel.getObject('app_auth_data_id',appAuthData)

            userInfo.first_name=request.POST['first_name']
            userInfo.last_name=request.POST['last_name']
            userInfo.save()

            userLog=UserLog()
            userLog.user_id = userInfo
            userLog.action = 'update first and last name'
            userLog.device_name=findDevice(request)
            userLog.save()

            data={'output':"yes"}
            myResponse=JsonResponse(data)
            return myResponse
           
           

def phoneExist(request):
    if request.method=="POST":
        phone_number=request.POST['phone_number']
        country_code=request.POST['country_code']
        data={}
        if AppAuthDataModel.getObject('phone_number',country_code+phone_number):
            data={'output':"yes"}
        else:            
           data={'output':"no"}
        return JsonResponse(data)


def emailExist(request):
    if request.method=="POST":
        email=request.POST['email']
        data={}
        if UserInfoModel.getObject('email',email):
            data={'output':"yes"}
        else:            
           data={'output':"no"}
        return JsonResponse(data)

def detail_tournament(request):
    if request.method=="POST":
        trn=tournament.objects.get(id=request.POST['trn_id'])
        data={}
        serialized_obj = serializers.serialize('json', [ trn, ])
        data={'trn':serialized_obj}
        return JsonResponse(data)

# ajax request for sending back all match info regarding particular tournament
# import array
def match_in_tournament(request):
    if request.method=="POST":
        print(request.POST['trn_id'])
        trn=tournament.objects.get(id=request.POST['trn_id'])
        matches=match.objects.all().filter(tournament=trn)

        team_home = []
        team_away = []
        match_thumbnail=[]
        for mat in matches:
            team_home.append(mat.team_home.name)
            team_away.append(mat.team_away.name)
           
        serializer = MatchSerializer(matches, many=True)
        data={'matches':serializer.data,'team_home':team_home,'team_away':team_away}
        return JsonResponse(data)
