# Generated by Django 4.1 on 2022-09-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_pics'),
    ]

    operations = [
        migrations.CreateModel(
            name='password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField(blank=True)),
                ('password_text', models.TextField(blank=True)),
            ],
        ),
    ]
