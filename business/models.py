# This files contains business logic for all the models

from models.models import *

class AppAuthDataModel:

    def save(self, appAuthDataEntity):
        appAuthData = AppAuthData(
            account_kit_id = appAuthDataEntity.account_kit_id,
            phone_number = appAuthDataEntity.phone_number
        )
        appAuthData.save()
        return appAuthData

    @staticmethod
    def getObject(attr,value):
        if attr=='phone_number':
            if AppAuthData.objects.all().filter(phone_number=value):
                return AppAuthData.objects.all().get(phone_number=value)
            else:
                return False
                
        elif attr=='account_kit_id':
            if AppAuthData.objects.all().filter(account_kit_id=value):
                return AppAuthData.objects.all().get(account_kit_id=value)
            else:
                return False

    # def delete(self,request):
    #     appAuthData = AppAuthData(
    #         account_kit_id = self.account_kit_id,
    #         phone_number = self.phone_number
    #     )  
    #     appAuthData.delete() 
         

class UserInfoModel:

    def save(self, userInfoEntity):
        userInfo = UserInfo(
            app_auth_data_id = userInfoEntity.app_auth_data_id,
            first_name = userInfoEntity.first_name,
            last_name = userInfoEntity.last_name,
            email = userInfoEntity.email,
            date_of_birth = userInfoEntity.date_of_birth,
            subscription_type_id = userInfoEntity.subscription_type_id,
            expiry_date = userInfoEntity.expiry_date,
            is_active = userInfoEntity.is_active
        )
        userInfo.save()
        return userInfo


    @staticmethod
    def getObject(attr,value):
        if attr=='app_auth_data_id':
            if UserInfo.objects.all().filter(app_auth_data_id=value):
                return UserInfo.objects.all().get(app_auth_data_id=value)
            else:
                return False

        elif attr=='email':
            if UserInfo.objects.all().filter(email=value):
                return UserInfo.objects.all().get(email=value)
            else:
                return False

        else:
            return False
                


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
    
    def save(self, notificationTypeEntity):
        notificationType = NotificationType(
            notify_on = notificationTypeEntity.notify_on
        )
        notificationType.save()
        return notificationType

    def get_all(self):
        return NotificationType.objects.all()    

class SubscriptionTypeModel:

    def save(self, subscriptionTypeEntity):
        subscriptionType = SubscriptionType(
            subscription = subscriptionTypeEntity.subscription
        )    
        subscriptionType.save()
        return subscriptionType

class CatchEmailTempModel:

    def __init__(self):
        self.id = 0
        self.email = ''

    def __init__(self,email):
        self.email = email

    def save(self):
        catchEmailTemp = catch_email_temp(
            email = self.email
        )
        catchEmailTemp.save()

    def delete(self):
        catchEmailTemp = catch_email_temp(
            email = self.email
        )
        catchEmailTemp.delete()            

class UserNotificationTypeModel:

    def save(self, userNotificationTypeEntity):
        userNotificationType = UserNotificationType(
            app_auth_data = userNotificationTypeEntitiy.app_auth_data,
            notification_type_id = userNotificationTypeEntitiy.notification_type_id
        )
        userNotificationType.save()
        return userNotificationType

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

class OrderModel:

    def save(self,OrderEntity):
        Order = Order(
            customer_id = OrderEntity.customer_id,
            order_id = OrderEntity.order_id,
            transaction_id=OrderEntity.transaction_id,
            transaction_status=OrderEntity.transaction_status
        )
        Order.save()
    
    @staticmethod
    def getObject(attr,value):
        if Order.objects.all().filter(order_id=value):
            return Order.objects.all().get(order_id=value)
        return False

class UserLogModel:

    def save(self,UserLogEntity):
        UserLog=UserLog(
            user_id = UserLogEntity.user_id,
            action = UserLogEntity.action,
            device_name = UserLog.device_name,
            date_time=UserLog.date_time,
        )
        UserLog.save()