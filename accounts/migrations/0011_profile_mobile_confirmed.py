# Generated by Django 3.1.7 on 2021-10-19 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20211016_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]