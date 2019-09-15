# This file contains entities for all the models
from django.utils.timezone import datetime

class AppAuthDataEntity:

    def __init__(self):
        self.id = 0
        self.account_kit_id = ''
        self.phone_number = ''

class UserInfoEntity:

    def __init__(self):
        self.id = 0
        self.app_auth_data_id = None
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.date_of_birth = ''
        self.subscription_type_id = 0
        self.expiry_date = None
        self.is_active = True

class TournamentEntity:

    def __init__(self):
        self.name = 0
        self.intro = ''
        self.tournament_detail_image = None
        self.color='#FF0000'
        self.organiser=None
        self.cnt_match=0
        self.start_date=datetime.datetime.now
        self.end_date=datetime.datetime.now
        self.venue=''

class MatchEntity:

    def __init__(self):
        self.team_home=None
        self.team_away=None
        self.tournament=None
        self.start_time=datetime.datetime.now
        self.end_time=datetime.datetime.now
        self.image=None
        self.winner=None
        self.home_score='0'
        self.away_score='0'
        self.boxcastLink=''

class NotificationType:

    def __init__(self):
        self.id = 0
        self.notify_on = ''

class UserNotificationTypeEntity:

    def __init__(self):
        self.id = 0
        self.app_auth_data = None
        self.notification_type_id = None

class OrderEntity:

    def __init__(self):
        self.customer_id = 0
        self.order_id = ''
        self.transaction_id=''
        self.transaction_status=False

class UserLogEntity:

    def __init(self):
        self.id=0
        self.user_id = 0
        self.action = ''
        self.device_name = ''
        self.date_time=datetime.now
