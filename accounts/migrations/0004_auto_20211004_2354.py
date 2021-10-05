# Generated by Django 3.1.7 on 2021-10-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211004_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='caste',
            field=models.CharField(default='HINDU', max_length=120),
        ),
        migrations.AddField(
            model_name='profile',
            name='religion',
            field=models.CharField(default='HINDU', max_length=120),
        ),
        migrations.AddField(
            model_name='profile',
            name='searchfor',
            field=models.CharField(default='HINDU', max_length=120),
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='profile1.png', upload_to='pics', verbose_name='static/vivah/img/profile.jpg'),
        ),
    ]
