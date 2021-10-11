# Generated by Django 3.1.7 on 2021-10-11 05:18

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Whatyouwant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60)),
                ('product_want', models.EmailField(max_length=260)),
                ('full_name', models.EmailField(max_length=70)),
                ('company_name', models.EmailField(max_length=120)),
                ('phone_number', models.EmailField(max_length=30)),
                ('type', models.EmailField(max_length=60)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_confirmed', models.BooleanField(default=False)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('birthplace', models.CharField(default='PUNE', max_length=100)),
                ('birthstate', models.CharField(default='MAHARASHTRA', max_length=100)),
                ('birthcountry', models.CharField(default='INDIA', max_length=100)),
                ('ampm', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', max_length=4)),
                ('languages', models.CharField(default='English', max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Male', max_length=10)),
                ('mobile', models.CharField(default='123456789', max_length=120)),
                ('religion', models.CharField(choices=[('Religion', 'Tamil'), ('Hindu', 'Hindu'), ('Muslim - Shia', 'Muslim - Shia'), ('Muslim - Sunni', 'Muslim - Sunni'), ('Muslim - Others', 'Muslim - Others'), ('Christian', 'Christian'), ('Sikh', 'Sikh'), ('Jain - Digambar', 'Jain - Digambar'), ('Jain - Shwetambar', 'Jain - Shwetambar'), ('Jain - Others', 'Jain - Others'), ('Parsi', 'Parsi'), ('Buddhist', 'Buddhist'), ('Inter-Religion', 'Inter - Religion'), ('Caste No Bar', 'Caste No Bar')], default='HINDU', max_length=50)),
                ('caste', models.CharField(default='HINDU', max_length=120)),
                ('searchfor', models.CharField(choices=[('Religion', 'Tamil'), ('Hindu', 'Hindu'), ('Muslim - Shia', 'Muslim - Shia'), ('Muslim - Sunni', 'Muslim - Sunni'), ('Muslim - Others', 'Muslim - Others'), ('Christian', 'Christian'), ('Sikh', 'Sikh'), ('Jain - Digambar', 'Jain - Digambar'), ('Jain - Shwetambar', 'Jain - Shwetambar'), ('Jain - Others', 'Jain - Others'), ('Parsi', 'Parsi'), ('Buddhist', 'Buddhist'), ('Inter-Religion', 'Inter - Religion'), ('Caste No Bar', 'Caste No Bar')], default='HINDU', max_length=50)),
                ('martialstatus', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed'), ('any status', 'Any Status')], default='Single', max_length=20)),
                ('img', models.ImageField(default='profile.jpg', upload_to='pics', verbose_name='static/pic/img/profile.jpg')),
                ('bio', models.CharField(blank=True, max_length=255, null=True)),
                ('aboutus', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.CharField(blank=True, max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('state', models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Chandigarh (UT)', 'Chandigarh (UT)'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('Pondicherry(UT)', 'Pondicherry(UT)'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=150, null=True)),
                ('zip', models.CharField(blank=True, max_length=30, null=True)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Verified'), (1, 'Unverified'), (2, 'Hold')], default=0)),
                ('videofile', models.FileField(default='videos/Krishna.mp4', null=True, upload_to='videos/', verbose_name='')),
                ('img1', models.ImageField(default='static/vivah/img/profile.jpg', upload_to='pics', verbose_name='Profile Image')),
                ('img2', models.ImageField(default='static/vivah/img/profile.jpg', upload_to='pics', verbose_name='Profile Image')),
                ('img3', models.ImageField(default='static/vivah/img/profile.jpg', upload_to='pics', verbose_name='Profile Image')),
                ('img4', models.ImageField(default='static/vivah/img/profile.jpg', upload_to='pics', verbose_name='Profile Image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilefo', models.CharField(choices=[('Myself', 'Myself'), ('Son', 'Son'), ('Daughter', 'Daughter'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Relative', 'Relative'), ('Friend', 'Friend')], default='Myself', max_length=20)),
                ('organization', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('pagemin', models.CharField(choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59'), ('60', '60')], default='30', max_length=20)),
                ('pagemax', models.CharField(choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59'), ('60', '60')], default='30', max_length=20)),
                ('pmartialstatus', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed'), ('any status', 'Any Status')], default='Single', max_length=20)),
                ('pcomplexion', models.CharField(choices=[('Fair', 'Fair'), ('Very Fair', 'Very Fair'), ('Medium', 'Medium'), ('Brown', 'Brown'), ('Dark', 'Dark'), ('Any Complexion', 'Any Complexion')], default='Fair', max_length=20)),
                ('preligion', models.CharField(choices=[('Religion', 'Tamil'), ('Hindu', 'Hindu'), ('Muslim - Shia', 'Muslim - Shia'), ('Muslim - Sunni', 'Muslim - Sunni'), ('Muslim - Others', 'Muslim - Others'), ('Christian', 'Christian'), ('Sikh', 'Sikh'), ('Jain - Digambar', 'Jain - Digambar'), ('Jain - Shwetambar', 'Jain - Shwetambar'), ('Jain - Others', 'Jain - Others'), ('Parsi', 'Parsi'), ('Buddhist', 'Buddhist'), ('Inter-Religion', 'Inter - Religion'), ('Caste No Bar', 'Caste No Bar')], default='HINDU', max_length=50)),
                ('peducation', models.CharField(choices=[('99', 'Bachelors - Engineering / Computers / Others'), ('100', 'Masters - Engineering / Computers / Others'), ('101', 'Bachelors - Arts / Science / Commerce / Others'), ('102', 'Masters - Arts / Science / Commerce / Others'), ('103', 'Bachelors - Management / Others '), ('104', 'Masters - Management / Others'), ('105', 'Bachelors - Medicine - General / Dental / Surgeon / Others'), ('106', 'Masters - Medicine - General / Dental / Surgeon / Others'), ('107', 'Bachelors - Legal / Others'), ('108', 'Masters - Legal / Others'), ('109', 'Finance - ICWAI / CA / CS / CFA / Others'), ('110', 'Service - IAS / IPS / IRS / IES / IFS / Others'), ('111', 'PhD'), ('112', 'Diploma / Others'), ('114', 'Higher Secondary / Secondary'), ('215', 'Others')], default='Bachelors - Engineering / Computers / Others', max_length=50)),
                ('pcaste', models.CharField(default='HINDU', max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='123456789', max_length=200)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('joined_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='ColdCoffe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('order_id', models.CharField(blank=True, max_length=100)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
