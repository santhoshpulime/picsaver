# Generated by Django 4.1 on 2022-09-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_user_password_usern'),
    ]

    operations = [
        migrations.AddField(
            model_name='pics',
            name='username',
            field=models.TextField(blank=True),
        ),
    ]