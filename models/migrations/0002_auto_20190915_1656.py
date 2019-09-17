# Generated by Django 2.2.2 on 2019-09-15 11:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='email_token',
            field=models.CharField(default='WIIZ4AgJKBPOyXDkR0opdaWLOqSo3CF0', max_length=32),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='token_expiry',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]