# Generated by Django 2.2.2 on 2019-09-02 20:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0013_auto_20190831_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='cnt_match',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tournament',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='tournament',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='tournament',
            name='venue',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email_token',
            field=models.CharField(default='fhJXZ2Q9URYGkd5jESGLdVwcN5tTFW2m', max_length=32),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='token_expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 2, 20, 8, 24, 763541, tzinfo=utc)),
        ),
    ]
