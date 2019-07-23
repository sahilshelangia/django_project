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

    def delete(self,request):
        appAuthData = AppAuthData(
            account_kit_id = self.account_kit_id,
            phone_number = self.phone_number
        )  
        appAuthData.delete()  

class UserInfoModel(AppAuthDataModel):

    def __init__(self):
        self.id = 0
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.date_of_birth = ''
        super(AppAuthDataModel).__init__()

    def __init__(self,first_name,last_name,email,date_of_birth,expiry_date,is_active):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_of_birth = date_of_birth
        self.expiry_date = expiry_date
        self.is_active = is_active
        super(AppAuthDataModel).__init__(self)

    def save(self):
        userInfo = UserInfo(
            first_name = self.first_name,
            last_name = self.last_name,
            email = self.email,
            date_of_birth = self.date_of_birth,
            expiry_date = self.expiry_date,
            is_active = self.is_active
        )
        userInfo.save()

    def delete(self):
        userInfo = UserInfo(
            first_name = self.first_name,
            last_name = self.last_name,
            email = self.email,
            date_of_birth = self.date_of_birth,
            expiry_date = self.expiry_date,
            is_active = self.is_active
        )
        userInfo.delete()

class NotificationTypeModel:
    
    def __init__(self):
        self.id = 0
        self.notify_on = ''

    def __init__(self,notify_on):
        self.notify_on = notify_on

    def save(self):
        notificationType = NotificationType(
            notify_on = self.notify_on
        )
        notificationType.save()

    def delete(self,request):
        notificationType = NotificationType(
            notify_on = self.notify_on
        )
        notificationType.delete()

class SubscriptionTypeModel:

    def __init__(self):
        self.id = 0
        self.subscription = ''

    def __init__(self,subscription):
        self.subscription = subscription

    def save(self):
        subscriptionType = SubscriptionType(
            subscription = self.subscription
        )    
        subscriptionType.save()

    def delete(self,request):
        subscriptionType = SubscriptionType(
            subscription = self.subscription
        )    
        subscriptionType.delete()

class CatchEmailTempModel:

    def __init__(self):
        self.id = 0
        self.email = ''

    def __init__(self,email):
        self.email = email

    def save(self):
        catchEmailTemp = CatchEmailTemp(
            email = self.email
        )
        catchEmailTemp.save()

    def delete(self):
        catchEmailTemp = CatchEmailTemp(
            email = self.email
        )
        catchEmailTemp.delete()            

class UserNotificationTypeModel:

    def __init__(self):
        self.id = 0
        super(UserInfoModel,NotificationTypeModel).__init__(self)  


