from models.models import *
from django.shortcuts import render, HttpResponse

import random
import string
import requests
import json

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
        data = request.body
        listData = data.decode().split(',')
        codeData = listData[1].split(':')
        code = codeData[1].replace('"', '')
        
        response = requests.get('https://graph.accountkit.com/v1.3/access_token?grant_type=authorization_code' \
            '&code=' + code + '&access_token=AA|374722036360552|b5623e49377b054de9e1149a2513fda1')
        access_data = response.text
        access_code = access_data.split(',')[1].split(':')[1].replace('"', '')

        response = requests.get('https://graph.accountkit.com/v1.3/me/?access_token=' + access_code)
        user_data = response.text.replace('"', '').replace('{', '').replace('}', '').replace(',', ':').split(':')
        account_kit_user_id = user_data[1]
        phone_numbers = user_data[4]

        exists = AppAuthData.objects.filter(account_kit_id = account_kit_user_id).exists()
        if exists:
            print('exists')
        else:
            appAuthData = AppAuthData(
                account_kit_id = account_kit_user_id,
                phone_number = phone_numbers
            )
            appAuthData.save()

        myResponse = HttpResponse()
        myResponse.set_cookie(key='goalstar', value=access_data, max_age=31536000, httponly=True)

        return myResponse