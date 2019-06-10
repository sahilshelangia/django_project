from django.db import models

# Create your models here.

# Model for storing authentication data
# Account kit id is receivedd in response
class AppAuthData(models.Model):
    account_kit_id = models.CharField(max_length = 25, unique = True)
    phone_number = models.CharField(max_length = 25, unique = True)

    class Meta:
        db_table = "app_auth_data"

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

    class Meta:
        db_table = "user_info"