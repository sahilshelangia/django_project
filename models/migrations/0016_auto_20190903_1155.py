# Generated by Django 2.2.2 on 2019-09-03 06:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0015_auto_20190903_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='email_token',
            field=models.CharField(default='flNWfhCT906FxYUjxmQSpZOgFjoccBGD', max_length=32),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='token_expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 3, 6, 25, 49, 462510, tzinfo=utc)),
        ),
    ]