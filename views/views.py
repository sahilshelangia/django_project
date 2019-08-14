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

def logout(request):
    dic = {
        'FACEBOOK_APP_ID': '374722036360552',
        'csrf': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(36)),
        'ACCOUNT_KIT_API_VERSION': 'v1.1'
    }
    myResponse = render(request,'login.html',dic)
    myResponse.delete_cookie('goalstar')
    return myResponse
    

def login(request):
<<<<<<< HEAD
    # use login in 
    if request.POST:
        accountkit_data = accountkit.validate_accountkit_access_token(accountkit.get_accountkit_access_token(request.POST['login_accountkit_data']))
        device=''
        if request.user_agent.is_mobile:
            device='mobile'

        if request.user_agent.is_tablet :
            device='tablet'
        
        if request.user_agent.is_pc:
            device='pc'

        myResponse = render(request,'home.html',{})
        
        # phone number,device Info
        phoneNumber=request.POST['login-code']+request.POST['login-phone']
        cookieInfo={'accountkit_data':accountkit_data,'device':device}
        myResponse.set_cookie(key='goalstar',value=cookieInfo,httponly=True,max_age=31536000)
        return myResponse

    else:
        if request.COOKIES.get('goalstar'):
            import ast
            cookie_dict=ast.literal_eval(request.COOKIES['goalstar'])
            myResponse = render(request,'home.html',{})
            return myResponse  
        else:
            dic = {
                'FACEBOOK_APP_ID': '374722036360552',
                'csrf': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(36)),
                'ACCOUNT_KIT_API_VERSION': 'v1.1'
            }
            return render(request, 'login.html', dic)


def authCode(request):
    if request.method == "POST":
        accountkit_data = accountkit.validate_accountkit_access_token(accountkit.get_accountkit_access_token(request.POST['accountkit_data']))
        appAuthData = AppAuthData(
                account_kit_id = accountkit_data[0],
                phone_number = accountkit_data[1]
            )
        appAuthData.save()


        # appAuthDataEntity=AppAuthDataEntity()
        # appAuthDataEntity.account_kit_id=accountkit_data[0]
        # appAuthDataEntity.phone_number=accountkit_data[1]

        # appAuthDataModel=AppAuthDataModel()
        # idd=appAuthDataModel.save(appAuthDataEntity)

        # create profile for the same
        
        userInfoModel=UserInfo(app_auth_data_id=appAuthData,first_name=request.POST['first_name'],\
            last_name=request.POST['last_name'],email=request.POST['email'],date_of_birth=request.POST['dob'],\
            subscription_type_id=SubscriptionType.objects.get(subscription="free"),expiry_date=datetime.date.today()+datetime.timedelta(days=90))
        userInfoModel.save()

        # userInfoEntity=UserInfoEntity()
        # userInfoEntity.app_auth_data_id=appAuthDataModel
        # userInfoEntity.first_name=request.POST['first_name']
        # userInfoEntity.last_name=request.POST['last_name']
        # userInfoEntity.email=request.POST['email']
        # userInfoEntity.date_of_birth=request.POST['dob']
        # userInfoEntity.subscription_type_id=SubscriptionType.objects.get(subscription="free")
        # userInfoEntity.expiry_date=datetime.date.today()+datetime.timedelta(days=90)
        # userInfoModel=UserInfoModel()
        # userInfoModel.save(userInfoEntity)

        # add notification to the same
        for obj in NotificationType.objects.all():
            userNotificationType=UserNotificationType(app_auth_data=appAuthData,notification_type_id=obj)
            userNotificationType.save()

        userLog=UserLog()
        userLog.user_id=userInfoModel
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
        cookieInfo={'accountkit_data':accountkit_data,'device':userLog.device_name}
        myResponse.set_cookie(key='goalstar',value=cookieInfo,httponly=True,max_age=31536000)
=======
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

>>>>>>> 22dd5159f7895ed4d3dd1fd953ce1de50a4b9fea
        return myResponse

def notify(request):
    if request.method == "POST":
        print(request.body)
        
        notify_me = catch_email_temp(
            email=str(request.body)
        )
        notify_me.save()


<<<<<<< HEAD
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
    myResponse = render(request,'home.html',{})
    return myResponse
=======
        return HttpResponse('')
>>>>>>> 22dd5159f7895ed4d3dd1fd953ce1de50a4b9fea
