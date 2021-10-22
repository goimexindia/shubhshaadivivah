# Generated by Django 3.1.7 on 2021-10-22 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20211021_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.CharField(blank=True, choices=[('99', 'Bachelors - Engineering / Computers / Others'), ('100', 'Masters - Engineering / Computers / Others'), ('101', 'Bachelors - Arts / Science / Commerce / Others'), ('102', 'Masters - Arts / Science / Commerce / Others'), ('103', 'Bachelors - Management / Others '), ('104', 'Masters - Management / Others'), ('105', 'Bachelors - Medicine - General / Dental / Surgeon / Others'), ('106', 'Masters - Medicine - General / Dental / Surgeon / Others'), ('107', 'Bachelors - Legal / Others'), ('108', 'Masters - Legal / Others'), ('109', 'Finance - ICWAI / CA / CS / CFA / Others'), ('110', 'Service - IAS / IPS / IRS / IES / IFS / Others'), ('111', 'PhD'), ('112', 'Diploma / Others'), ('114', 'Higher Secondary / Secondary'), ('215', 'Others')], max_length=50, null=True),
        ),
    ]
