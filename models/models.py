from django.db import models
from django.utils.timezone import datetime
from colorfield.fields import ColorField
# Create your models here.

# Model for storing authentication data
# Account kit id is receivedd in response
class AppAuthData(models.Model):
    account_kit_id = models.CharField(max_length = 25, unique = True)
    phone_number = models.CharField(max_length = 25, unique = True)

    class Meta:
        db_table = "app_auth_data"

# Model which stores notification types
class NotificationType(models.Model):
    notify_on = models.CharField(max_length = 25)

    class Meta:
        db_table = "notification_type"

# Model which stores subscription types
class SubscriptionType(models.Model):
    subscription = models.CharField(max_length = 25)

    class Meta:
        db_table = "subscription_type"

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
    date_of_birth = models.DateField()
    subscription_type_id = models.ForeignKey(
        SubscriptionType,
        on_delete = models.CASCADE,
        default = 1
    )
    expiry_date = models.DateField(blank = True, null = True)
    is_active = models.BooleanField(default = True)

    class Meta:
        db_table = "user_info"

class UserNotificationType(models.Model):
    user_info_id = models.ForeignKey(
        UserInfo,
        on_delete = models.CASCADE
    )
    notification_type_id = models.ForeignKey(
        NotificationType,
        on_delete = models.CASCADE
    )

    class Meta:
        db_table = "user_notification_type"

class catch_email_temp(models.Model):
    email = models.CharField(max_length = 50)

    class Meta:
        db_table = "catch_email_temp"





class organiser(models.Model):
    name= models.CharField(max_length=128)
    role=models.CharField(max_length=128)
    company=models.CharField(max_length=128)
    phone=models.CharField(max_length=16)
    organiser_email=models.EmailField()

    class Meta:
        db_table = "organiser"

    def __str__(self):
        return self.name


class team(models.Model):
    name=models.CharField(max_length=128)
    logo=models.ImageField(upload_to='team_logo')
    owner=models.CharField(max_length=128)
    manager=models.CharField(max_length=128)

    class Meta:
        db_table = "team"

    def __str__(self):
        return self.name

class player(models.Model):
    name=models.CharField(max_length=64)
    position=models.CharField(max_length=64)
    jersey_number=models.CharField(max_length=16)
    team=models.ForeignKey(team,on_delete=models.CASCADE)
    class Meta:
        db_table = "player"

    def __str__(self):
        return self.name 

class tournament(models.Model):
    name=models.CharField(max_length=64)
    intro=models.TextField()
    tournament_detail_image=models.ImageField(upload_to='tournament_image',blank=True)
    color=ColorField(default='#FF0000')
    organiser=models.ForeignKey(organiser,on_delete=models.CASCADE)
    class Meta:
        db_table = "tournament"

    def __str__(self):
        return self.name 

class tournament_team_relationship(models.Model):
    tournament=models.ForeignKey(tournament,on_delete=models.CASCADE)
    team=models.ForeignKey(team,on_delete=models.CASCADE)

    class Meta:
        db_table='tournament_team_relationship'
        unique_together = (('tournament', 'team'),)


class match(models.Model):
    team_home=models.ForeignKey(team,related_name='team_home',on_delete=models.CASCADE)
    team_away=models.ForeignKey(team,related_name='team_away',on_delete=models.CASCADE)
    tournament=models.ForeignKey(tournament,related_name='tournament',on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    venue=models.CharField(max_length=256)
    image=models.ImageField(upload_to='match_images')
    winner=models.ForeignKey(team,related_name='team_winner',on_delete=models.CASCADE,default="Not Declared")
    home_score=models.CharField(max_length=4)
    away_score=models.CharField(max_length=4)

    class Meta:
        db_table = "match"

    def __str__(self):
        return '{} vs {}'.format(self.team_home,self.team_away)