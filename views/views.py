from models.models import *
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse,redirect
from business import accountkit
from business.models import *
from business.entities import *
import random
import string
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    if request.COOKIES.get('goalstar'):
        import ast
        cookie_dict=ast.literal_eval(request.COOKIES['goalstar'])
        appAuthData=AppAuthData.objects.all().filter(phone_number=cookie_dict['accountkit_data'][1])[0]
        userInfo=UserInfo.objects.all().filter(app_auth_data_id=appAuthData)[0]
        context={'userInfo':userInfo}
        myResponse = render(request,'home.html',context=context)
        return myResponse 
    else:
        return redirect('login')

# logout using delete cookies
def logout(request):
    # first check user is already logged in or not
    if request.COOKIES.get('goalstar'):
        import ast
        cookie_dict=ast.literal_eval(request.COOKIES['goalstar'])
        appAuthData=AppAuthData.objects.all().filter(phone_number=cookie_dict['accountkit_data'][1])[0]
        userInfo=UserInfo.objects.all().filter(app_auth_data_id=appAuthData)[0]
        device=''
        if request.user_agent.is_mobile:
            device='mobile'

        if request.user_agent.is_tablet :
            device='tablet'
        
        if request.user_agent.is_pc:
            device='pc'

        # log the user action
        userLog=UserLog()
        userLog.user_id=userInfo
        userLog.action='logout'
        userLog.device_name=device
        userLog.save()

        myResponse = redirect('login')
        myResponse.delete_cookie('goalstar')
        return myResponse
    

def login(request):
    # We have three cases for login
    # This is when user submit login form and trying to login we will use this one
    if request.POST:
        accountkit_data = accountkit.validate_accountkit_access_token(accountkit.get_accountkit_access_token(request.POST.get('login_accountkit_data')))
        device=''
        if request.user_agent.is_mobile:
            device='mobile'

        if request.user_agent.is_tablet :
            device='tablet'
        
        if request.user_agent.is_pc:
            device='pc'

        appAuthData=AppAuthData.objects.all().filter(phone_number=accountkit_data[1])[0]
        userInfo=UserInfo.objects.all().filter(app_auth_data_id=appAuthData)[0]
        # context={'userInfo':userInfo}
        # myResponse = render(request,'home.html',context=context)
        

        # phone number,device Info
        userLog=UserLog(user_id=userInfo,action='login',device_name=device)
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
        if request.user_agent.is_mobile:
            userLog.device_name='mobile'

        if request.user_agent.is_tablet :
            userLog.device_name='tablet'
        
        if request.user_agent.is_pc:
            userLog.device_name='pc'
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
        data={}
        if AppAuthData.objects.all().filter(phone_number=country_code+phone_number):
            data={'output':"yes"}
        else:            
           data={'output':"no"}
        return JsonResponse(data)

def checkBuisness(request):
    print(AppAuthData.objects.all())
    return HttpResponse('done')


def updateEmail(request):
    if request.method=="POST":
        if request.COOKIES.get('goalstar'):
            import ast
            cookie_dict=ast.literal_eval(request.COOKIES['goalstar'])
            appAuthData=AppAuthData.objects.all().filter(phone_number=cookie_dict['accountkit_data'][1])[0]
            userInfo=UserInfo.objects.all().filter(app_auth_data_id=appAuthData)[0]
            userInfo.email=request.POST['email']
            userInfo.save()
            data={'output':"successful"}
            return JsonResponse(data)
        else:
            return HttpResponse("Permission Denied!!!")

def updatePhone(request):
    if request.method=="POST":
        if request.COOKIES.get('goalstar'):
            import ast
            cookie_dict=ast.literal_eval(request.COOKIES['goalstar'])
            appAuthData=AppAuthData.objects.all().filter(phone_number=cookie_dict['accountkit_data'][1])[0]
            appAuthData.phone_number=request.POST['phone']
            appAuthData.save()

            # update cookie as well
            data={'output':"successful"}
            return JsonResponse(data)
        else:
            return HttpResponse("Permission Denied!!!")