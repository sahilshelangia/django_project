# Generated by Django 2.2.2 on 2019-08-31 09:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0012_auto_20190831_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='email_token',
            field=models.CharField(default='QlQGd1556nniLTdrSt5rxHgbKXkQfIWc', max_length=32),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='token_expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 31, 9, 9, 33, 426354, tzinfo=utc)),
        ),
    ]