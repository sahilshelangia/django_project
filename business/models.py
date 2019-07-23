# This files contains business logic for all the models

from models.models import *

class AppAuthDataModel:

    def __init__(self):
        self.id = 0
        self.account_kit_id = ''
        self.phone_number = ''

    def __init__(self, account_kit_id, phone_number):
        self.account_kit_id = account_kit_id
        self.phone_number = phone_number

    def save(self):
        appAuthData = AppAuthData(
            account_kit_id = self.account_kit_id,
            phone_number = self.phone_number
        )
        appAuthData.save()

class UserInfoModel(AppAuthDataModel):

    def __init__(self):
        self.id = 0
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.date_of_birth = ''
        super(AppAuthDataModel).__init__()