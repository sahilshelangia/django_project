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
    def changeEmail(id,email):
        userInfo=UserInfo.objects.get(id=id)
        userInfo.email=email
        userInfo.email_verified=False
        userInfo.save()

    @staticmethod
    def changeName(id,first_name,last_name):
        userInfo=UserInfo.objects.get(id=id)
        userInfo.first_name=first_name
        userInfo.last_name=last_name
        userInfo.save()

    @staticmethod
    def updateEmailToken(id):
        userInfo=UserInfo.objects.get(id=id)
        userInfo.email_token=get_random_string(length=32)
        userInfo.token_expiry=timezone.now()+timezone.timedelta(hours=1)
        userInfo.save()

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

class TournamentModel:
    def save(self, TournamentEntity):
        tournament = Tournament(
            name=TournamentEntity.name,
            intro=TournamentEntity.intro,
            tournament_detail_image=TournamentEntity.tournament_detail_image,
            color=TournamentEntity.color,
            cnt_match=TournamentEntity.cnt_match,
            start_date=TournamentEntity.start_date,
            end_date=TournamentEntity.end_date,
            venue=TournamentEntity.venue
        )
        tournament.save()
        return userInfo

    @staticmethod
    def getAllObject():
        return Tournament.objects.all()

    @staticmethod
    def getObject(attr,value):
        if attr=='id':
            if Tournament.objects.all().filter(id=value):
                return Tournament.objects.all().get(id=value)
            else:
                return False


class MatchModel:
    def save(self, MatchEntity):
        match = Match(
            team_home=MatchEntity.team_home,
            team_away=MatchEntity.team_away,
            tournament=MatchEntity.tournament,
            start_time=MatchEntity.start_time,
            end_time=MatchEntity.end_time,
            image=MatchEntity.image,
            winner=MatchEntity.winner,
            home_score=MatchEntity.home_score,
            away_score=MatchEntity.away_score,
            boxcastLink=MatchEntity.boxcastLink
        )
        match.save()
        return match

    @staticmethod
    def getAllObject():
        return Match.objects.all()

    @staticmethod
    def getObject(attr,value):
        if attr=='tournament':
            if Match.objects.all().filter(tournament=value):
                return Match.objects.all().filter(tournament=value)
            else:
                return False

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields='__all__'

class CarouselModel:
    def save(self, CarouselEntity):
        carousel=Carousel(
            carousel_image = CarouselEntity.carousel_image,
            carousel_image_mobile = CarouselEntity.carousel_image_mobile,
            video_link = CarouselEntity.video_link,
            match_opponent1 = CarouselEntity.match_opponent1,
            match_opponent2 = CarouselEntity.match_opponent2,
            active_option = CarouselEntity.active_option
        )
        carousel.save()
        return carousel

    @staticmethod
    def getAllObject():
        return Carousel.objects.all()
