# Generated by Django 3.1.7 on 2021-10-11 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_profile_profilefo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='pmartialstatus',
            field=models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('waiting for divorced', 'Waiting For Divorced'), ('widowed', 'Widowed'), ('any status', 'Any Status')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthstate',
            field=models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Chandigarh (UT)', 'Chandigarh (UT)'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('Pondicherry(UT)', 'Pondicherry(UT)'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], default='MAHARASHTRA', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='languages',
            field=models.CharField(choices=[('Bengali', 'Bengali'), ('Gujarati', 'Gujarati'), ('Hindi', 'Hindi'), ('Kannada', 'Kannada'), ('Malayalam', 'Malayalam'), ('Marathi', 'Marathi'), ('Marwari', 'Marwari'), ('Oriya', 'Oriya'), ('Punjabi', 'Punjabi'), ('Sindhi', 'Sindhi'), ('Tamil', 'Tamil'), ('Telugu', 'Telugu'), ('Urdu', 'Urdu')], default='Hindi', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='martialstatus',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('waiting for divorced', 'Waiting For Divorced'), ('widowed', 'Widowed'), ('any status', 'Any Status')], default='Single', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profilefo',
            field=models.CharField(choices=[('Myself', 'Myself'), ('Son', 'Son'), ('Daughter', 'Daughter'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Relative', 'Relative'), ('Friend', 'Friend')], default='Myself', max_length=20),
        ),
        migrations.CreateModel(
            name='FamilyValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(blank=True, choices=[('4-6', '4ft 6in / 137 cms'), ('4-7', '4ft 7in / 139 cms'), ('4-8', '4ft 8in / 142 cms'), ('4-9', '4ft 9in / 144 cms'), ('4-10', '4ft 10in / 147 cms'), ('4-11', '4ft 11in / 149 cms'), ('5', '5ft / 152 cms'), ('5-1', '5ft 1in / 154 cms'), ('5-2', '5ft 2in / 157 cms'), ('5-3', '5ft 3in / 160 cms'), ('5-4', '5ft 4in / 162 cms'), ('5-5', '5ft 5in / 165 cms'), ('5-6', '5ft 6in / 167 cms'), ('5-7', '5ft 7in / 170 cms'), ('5-8', '5ft 8in / 172 cms'), ('5-9', '5ft 9in / 175 cms'), ('5-10', '5ft 10in / 177cms'), ('5-11', '5ft 11in / 180 cms'), ('6', '6ft / 182 cms'), ('6-1', '6ft 1 in / 185 cms'), ('6-2', '6ft 2in / 187 cms'), ('6-3', '6ft 3in / 190 cms'), ('6-4', '6ft 4in / 193 cms'), ('6-5', '6ft 5in / 195 cms'), ('6-6', '6ft 6in / 198 cms')], max_length=20, null=True)),
                ('familystatus', models.CharField(blank=True, choices=[('Middle Class', 'Middle Class'), ('Upper Middle Class', 'Upper Middle Class'), ('Rich', 'Rich'), ('Elite', 'Elite')], max_length=30, null=True)),
                ('familytype', models.CharField(blank=True, choices=[('Nuclear', 'Nuclear'), ('Joint', 'Joint')], max_length=30, null=True)),
                ('familyvalues', models.CharField(blank=True, choices=[('Orthodox', 'Orthodox'), ('Tradational', 'Tradational'), ('Moderate', 'Moderate'), ('Liberal', 'Liberal')], max_length=30, null=True)),
                ('disability', models.CharField(blank=True, max_length=30, null=True)),
                ('employed', models.CharField(blank=True, choices=[('Self Employed', 'Self Employed'), ('Business', 'Business'), ('Government', 'Government'), ('PSU', 'PSU'), ('MNC', 'MNC'), ('Defence', 'Defence'), ('Private', 'Private'), ('Not Working', 'Not Working')], max_length=30, null=True)),
                ('designation', models.CharField(blank=True, max_length=30, null=True)),
                ('annualincome', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]