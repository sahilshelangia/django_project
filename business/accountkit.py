# This file should contain only static definitions
# This file contains definitions related to Facebook's Account Kit.

import requests
import json

# Function to retrieve for facebook app id
def get_facebook_app_id():
    
    return '374722036360552'

# Function to retrieve for account kit api version
def get_accountkit_api_version():

    return 'v1.1'

# Function to retrieve for account kit api secret
def get_accountkit_app_secret():

    return 'b5623e49377b054de9e1149a2513fda1'

# Function to retrieve access token using Graph API
def get_accountkit_access_token(data):

    json_data = json.loads(data)
    response = requests.get('https://graph.accountkit.com/v1.3/access_token?grant_type=authorization_code' \
        '&code=' + json_data['code'] + '&access_token=AA|'+ get_facebook_app_id() + '|' + get_accountkit_app_secret())
    access_code = json.loads(response.text)['access_token']

    return access_code

# Function to validate access token and retrieve account kit id and phone number
def validate_accountkit_access_token(token):

    response = requests.get('https://graph.accountkit.com/v1.3/me/?access_token=' + token)
    json_data = json.loads(response.text)
    # phone = json.loads(json_data['phone']).number

    return [json_data['id'], json_data['phone']['number']]