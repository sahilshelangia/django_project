# Generated by Django 2.2.1 on 2019-06-09 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppAuthData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_kit_id', models.IntegerField()),
                ('phone_number', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'app_auth_data',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=45)),
                ('date_of_birth', models.DateField()),
                ('app_auth_data_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.AppAuthData')),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]