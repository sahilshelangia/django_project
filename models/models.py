from django.db import models
from django.utils.timezone import datetime
from colorfield.fields import ColorField
import datetime
from django.utils.crypto import get_random_string
from django.utils import timezone
from rest_framework import serializers

# Create your models here.

# Model for storing authentication data
# Account kit id is received in response
class AppAuthData(models.Model):
    account_kit_id = models.CharField(max_length = 25, unique = True)
    phone_number = models.CharField(max_length = 25, unique = True)

    class Meta:
        db_table = "app_auth_data"

    def __str__(self):
        return self.phone_number


# Model which stores notification types
# sms,whatsapp,email
# many to many relationship with user Info
class NotificationType(models.Model):
    
    notify_on = models.CharField(max_length = 25)

    class Meta:
        db_table = "notification_type"

    def __str__(self):
        return self.notify_on


# Model which stores subscription types
# free(default,3 months), monthly ,seasonal
class SubscriptionType(models.Model):
    subscription = models.CharField(max_length = 25)

    class Meta:
        db_table = "subscription_type"

    def __str__(self):
        return self.subscription


# Model for storing user info
# app_auth_data_id links the user with authentication information
class UserInfo(models.Model):
    app_auth_data_id = models.ForeignKey(
        AppAuthData,
        on_delete = models.CASCADE,
    )
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    email = models.CharField(max_length = 65, unique = True)
    email_verified=models.BooleanField(default=False)
    email_token=models.CharField(max_length=32,default=get_random_string(length=32))
    token_expiry=models.DateTimeField(default=timezone.now)
    date_of_birth = models.DateField()
    subscription_type_id = models.ForeignKey(
        SubscriptionType,
        on_delete = models.CASCADE,
        default = 1
    )
    expiry_date = models.DateField(null=True,blank=True)
    is_active = models.BooleanField(default = True)

    class Meta:
        db_table = "user_info"

    def __str__(self):
        return self.first_name+" "+self.last_name


# connect userid with all notification type by default
class UserNotificationType(models.Model):
    app_auth_data = models.ForeignKey(
        AppAuthData,
        on_delete = models.CASCADE
    )
    notification_type_id = models.ForeignKey(
        NotificationType,
        on_delete = models.CASCADE
    )

    class Meta:
        db_table = "user_notification_type"

    def __str__(self):
        return "{}=>{}".format(self.app_auth_data,self.notification_type_id)



class catch_email_temp(models.Model):
    email = models.CharField(max_length = 50)

    class Meta:
        db_table = "catch_email_temp"



class Organiser(models.Model):
    name= models.CharField(max_length=128)
    role=models.CharField(max_length=128)
    company=models.CharField(max_length=128)
    phone=models.CharField(max_length=16)
    organiserEmail=models.EmailField()

    class Meta:
        db_table = "organiser"

    def __str__(self):
        return self.name


class Team(models.Model):
    name=models.CharField(max_length=128)
    logo=models.ImageField(upload_to='team_logo')
    owner=models.CharField(max_length=128)
    manager=models.CharField(max_length=128)

    class Meta:
        db_table = "team"

    def __str__(self):
        return self.name

class Player(models.Model):
    name=models.CharField(max_length=64)
    position=models.CharField(max_length=64)
    jersey_number=models.CharField(max_length=16)
    team=models.ForeignKey(Team,on_delete=models.CASCADE)
    class Meta:
        db_table = "player"

    def __str__(self):
        return self.name 

class Tournament(models.Model):
    name=models.CharField(max_length=64)
    intro=models.TextField()
    tournament_detail_image=models.ImageField(upload_to='tournament_image',blank=True)
    # thumnail image
    color=ColorField(default='#FF0000')
    organiser=models.ForeignKey(Organiser,on_delete=models.CASCADE)
    cnt_match=models.IntegerField(default=0)
    start_date=models.DateTimeField(default=datetime.datetime.now)
    end_date=models.DateTimeField(default=datetime.datetime.now)
    venue=models.CharField(max_length=256,default="")

    class Meta:
        db_table = "tournament"

    def __str__(self):
        return self.name 

class TournamentTeamRelationship(models.Model):
    tournament=models.ForeignKey(Tournament,on_delete=models.CASCADE)
    team=models.ForeignKey(Team,on_delete=models.CASCADE)

    class Meta:
        db_table='tournament_team_relationship'
        unique_together = (('tournament', 'team'),)


class Match(models.Model):
    team_home=models.ForeignKey(Team,related_name='team_home',on_delete=models.CASCADE)
    team_away=models.ForeignKey(Team,related_name='team_away',on_delete=models.CASCADE)
    tournament=models.ForeignKey(Tournament,related_name='tournament',on_delete=models.CASCADE)
    start_time=models.DateTimeField(default=datetime.datetime.now)
    end_time=models.DateTimeField(default=datetime.datetime.now)
    image=models.ImageField(upload_to='match_images')
    winner=models.ForeignKey(Team,related_name='team_winner',on_delete=models.CASCADE,default="Not Declared")
    home_score=models.CharField(max_length=4,blank=True,null=True)
    away_score=models.CharField(max_length=4,blank=True,null=True)
    boxcastLink=models.CharField(max_length=10000,blank=True,null=True)
    class Meta:
        db_table = "match"

    def __str__(self):
        return '{} vs {}'.format(self.team_home,self.team_away)



#Model for User Log
class UserLog(models.Model):
    user_id = models.ForeignKey(UserInfo,on_delete = models.CASCADE)
    action = models.CharField(max_length=30)
    device_name = models.CharField(max_length=30)
    date_time=models.DateTimeField(default=datetime.datetime.now,blank=True,null=True)
    class Meta:
        db_table = "user_log"

    def __str__(self):
        return '{} done {} with {} at {}'.format(self.user_id,self.action,self.device_name,self.date_time)

#Model for Payment Order Holder
class Order(models.Model):
    customer_id = models.ForeignKey(UserInfo,on_delete = models.CASCADE)
    order_id=models.CharField(max_length=10)
    transaction_id=models.CharField(max_length=100)
    transaction_status=models.BooleanField(default=False)
    class Meta:
        db_table = "order_details"

    def __str__(self):
        return '{} by {}'.format(self.order_id,self.customer_id)

#Model for adding video links and the background image in the carousel
class Carousel(models.Model):
    carousel_image = models.ImageField(upload_to='carousel_images',blank=True)
    carousel_image_mobile = models.ImageField(upload_to='carousel_images_mobile',blank=True)
    video_link = models.CharField(max_length=255,default=None)
    match_opponent1 = models.CharField(max_length=20)
    match_opponent2 = models.CharField(max_length=20)
    active_option = models.BooleanField(default=False)
    class Meta:
        db_table = "carousel_details"
    
    def __str__(self):
        return '{} vs {}'.format(self.match_opponent1,self.match_opponent2)