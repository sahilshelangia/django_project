# This files contains business logic for all the models

from models.models import *

class AppAuthDataModel:

    def save(self, appAuthDataEntity):
        appAuthData = AppAuthData(
            account_kit_id = appAuthDataEntity.account_kit_id,
            phone_number = appAuthDataEntity.phone_number
        )
        appAuthData.save()
        return appAuthData.id

    # def delete(self,request):
    #     appAuthData = AppAuthData(
    #         account_kit_id = self.account_kit_id,
    #         phone_number = self.phone_number
    #     )  
    #     appAuthData.delete() 
         

class UserInfoModel:

    def save(self, userInfoEntity):
        userInfo = UserInfo(
            app_auth_data_id = userInfoEntity.id,
            first_name = userInfoEntity.first_name,
            last_name = userInfoEntity.last_name,
            email = userInfoEntity.email,
            date_of_birth = userInfoEntity.date_of_birth,
            subscription_type_id = userInfoEntity.subscription_type_id,
            expiry_date = userInfoEntity.expiry_date,
            is_active = userInfoEntity.is_active
        )
        userInfo.save()

    # def delete(self):
    #     userInfo = UserInfo(
    #         first_name = self.first_name,
    #         last_name = self.last_name,
    #         email = self.email,
    #         date_of_birth = self.date_of_birth,
    #         expiry_date = self.expiry_date,
    #         is_active = self.is_active
    #     )
    #     userInfo.delete()

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

class UserLogModel:

    def __init__(self):
        self.user_id = 0
        self.action = ''
        self.device_name = ''

    def save(self):
        userLog = UserLog(
            user_id = self.user_id,
            action = self.action,
            device_name = self.device_name
        )
        userLog.save()
