from django.db import models

# Create your models here.

# Model for storing authentication data
# Account kit id is received in response
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