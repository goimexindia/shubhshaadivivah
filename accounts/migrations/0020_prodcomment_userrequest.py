# Generated by Django 3.1.7 on 2021-10-31 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20211031_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodcomment',
            name='userrequest',
            field=models.IntegerField(default=0),
        ),
    ]
