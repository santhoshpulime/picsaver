# Generated by Django 4.1 on 2022-09-11 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='password',
            old_name='user',
            new_name='usern',
        ),
    ]
