# Generated by Django 3.1.7 on 2021-10-11 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ampm',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birthcountry',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birthplace',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birthstate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birthtimehh',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birthtimemm',
        ),
    ]
