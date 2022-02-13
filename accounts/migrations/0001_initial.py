# Generated by Django 3.1.7 on 2022-02-13 15:01

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
            name='ColdCoffe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('order_id', models.CharField(blank=True, max_length=100)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(default='123456789', max_length=120)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ViewComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('userrequest', models.IntegerField(default=0)),
                ('userview', models.IntegerField(default=0)),
            ],
        ),
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
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilefo', models.CharField(choices=[('Myself', 'Myself'), ('Son', 'Son'), ('Daughter', 'Daughter'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Relative', 'Relative'), ('Friend', 'Friend')], default='Myself', max_length=20)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('mobile_confirmed', models.BooleanField(default=False)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('birthtimehh', models.CharField(blank=True, choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=10, null=True)),
                ('birthtimemm', models.CharField(blank=True, choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59'), ('60', '60')], max_length=10, null=True)),
                ('birthplace', models.CharField(default='PUNE', max_length=100)),
                ('birthstate', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Chandigarh (UT)', 'Chandigarh (UT)'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('Pondicherry(UT)', 'Pondicherry(UT)'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], default='MAHARASHTRA', max_length=100)),
                ('birthcountry', models.CharField(default='INDIA', max_length=100)),
                ('ampm', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', max_length=4)),
                ('languages', models.CharField(choices=[('Bengali', 'Bengali'), ('Gujarati', 'Gujarati'), ('Hindi', 'Hindi'), ('Kannada', 'Kannada'), ('Malayalam', 'Malayalam'), ('Marathi', 'Marathi'), ('Marwari', 'Marwari'), ('Oriya', 'Oriya'), ('Punjabi', 'Punjabi'), ('Sindhi', 'Sindhi'), ('Tamil', 'Tamil'), ('Telugu', 'Telugu'), ('Urdu', 'Urdu')], default='Hindi', max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Male', max_length=10)),
                ('mobile', models.CharField(default='123456789', max_length=120)),
                ('religion', models.CharField(choices=[('Religion', 'Tamil'), ('Hindu', 'Hindu'), ('Muslim - Shia', 'Muslim - Shia'), ('Muslim - Sunni', 'Muslim - Sunni'), ('Muslim - Others', 'Muslim - Others'), ('Christian', 'Christian'), ('Sikh', 'Sikh'), ('Jain - Digambar', 'Jain - Digambar'), ('Jain - Shwetambar', 'Jain - Shwetambar'), ('Jain - Others', 'Jain - Others'), ('Parsi', 'Parsi'), ('Buddhist', 'Buddhist'), ('Inter-Religion', 'Inter - Religion'), ('Caste No Bar', 'Caste No Bar')], default='HINDU', max_length=50)),
                ('caste', models.CharField(default='HINDU', max_length=120)),
                ('eventday', models.CharField(default='NO', max_length=10)),
                ('session', models.CharField(default='NO', max_length=10)),
                ('searchfor', models.CharField(choices=[('Religion', 'Tamil'), ('Hindu', 'Hindu'), ('Muslim - Shia', 'Muslim - Shia'), ('Muslim - Sunni', 'Muslim - Sunni'), ('Muslim - Others', 'Muslim - Others'), ('Christian', 'Christian'), ('Sikh', 'Sikh'), ('Jain - Digambar', 'Jain - Digambar'), ('Jain - Shwetambar', 'Jain - Shwetambar'), ('Jain - Others', 'Jain - Others'), ('Parsi', 'Parsi'), ('Buddhist', 'Buddhist'), ('Inter-Religion', 'Inter - Religion'), ('Caste No Bar', 'Caste No Bar')], default='HINDU', max_length=50)),
                ('martialstatus', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('waiting for divorced', 'Waiting For Divorced'), ('widowed', 'Widowed'), ('any status', 'Any Status'), ('never married', 'Never Married'), ('annulled', 'Annulled')], default='Single', max_length=20)),
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
                ('age', models.CharField(choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59'), ('60', '60')], default=30, max_length=20)),
                ('manglik', models.CharField(choices=[('Manglik', 'Manglik'), ('Non-manglik', 'Non-manglik'), ('Ashik manglik', 'Ashik manglik')], default='Non-manglik', max_length=20)),
                ('horo', models.CharField(choices=[('Must', 'Must'), ('Not Necessary', 'Not Necessary')], default=0, max_length=20)),
                ('smoke', models.IntegerField(choices=[(0, 'NO'), (1, 'YES'), (2, 'SOMETIMES')], default=0)),
                ('diet', models.CharField(choices=[('Veg', 'Veg'), ('Non-Veg', 'Non-Veg'), ('Occasionally NonVeg', 'Occasionally NonVeg'), ('Eggetarian', 'Eggetarian'), ('Jain', 'Jain'), ('Vegan', 'Vegan')], default='Veg', max_length=20)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('education', models.CharField(blank=True, choices=[('99', 'Bachelors - Engineering / Computers / Others'), ('100', 'Masters - Engineering / Computers / Others'), ('101', 'Bachelors - Arts / Science / Commerce / Others'), ('102', 'Masters - Arts / Science / Commerce / Others'), ('103', 'Bachelors - Management / Others '), ('104', 'Masters - Management / Others'), ('105', 'Bachelors - Medicine - General / Dental / Surgeon / Others'), ('106', 'Masters - Medicine - General / Dental / Surgeon / Others'), ('107', 'Bachelors - Legal / Others'), ('108', 'Masters - Legal / Others'), ('109', 'Finance - ICWAI / CA / CS / CFA / Others'), ('110', 'Service - IAS / IPS / IRS / IES / IFS / Others'), ('111', 'PhD'), ('112', 'Diploma / Others'), ('114', 'Higher Secondary / Secondary'), ('215', 'Others')], max_length=50, null=True)),
                ('videofile', models.FileField(default='videos/Krishna.mp4', null=True, upload_to='videos/', verbose_name='')),
                ('img1', models.ImageField(default='static/vivah/img/profile.jpg', upload_to='pics', verbose_name='Profile Image')),
                ('img2', models.ImageField(default='static/vivah/img/profile.jpg', upload_to='pics', verbose_name='Profile Image')),
                ('img3', models.ImageField(default='static/vivah/img/profile.jpg', upload_to='pics', verbose_name='Profile Image')),
                ('img4', models.ImageField(default='static/vivah/img/profile.jpg', upload_to='pics', verbose_name='Profile Image')),
                ('likes', models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='ProdComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('mobile', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('userrequest', models.IntegerField(default=0)),
                ('is_read', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prodcomment', to='accounts.profile')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilefo', models.CharField(blank=True, choices=[('Myself', 'Myself'), ('Son', 'Son'), ('Daughter', 'Daughter'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Relative', 'Relative'), ('Friend', 'Friend')], max_length=20, null=True)),
                ('organization', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('pagemin', models.CharField(blank=True, choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59'), ('60', '60')], max_length=20, null=True)),
                ('pagemax', models.CharField(blank=True, choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59'), ('60', '60')], max_length=20, null=True)),
                ('pmartialstatus', models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('waiting for divorced', 'Waiting For Divorced'), ('widowed', 'Widowed'), ('any status', 'Any Status'), ('never married', 'Never Married'), ('annulled', 'Annulled')], max_length=20, null=True)),
                ('pcomplexion', models.CharField(blank=True, choices=[('Fair', 'Fair'), ('Very Fair', 'Very Fair'), ('Medium', 'Medium'), ('Brown', 'Brown'), ('Dark', 'Dark'), ('Any Complexion', 'Any Complexion')], max_length=20, null=True)),
                ('preligion', models.CharField(blank=True, choices=[('Religion', 'Tamil'), ('Hindu', 'Hindu'), ('Muslim - Shia', 'Muslim - Shia'), ('Muslim - Sunni', 'Muslim - Sunni'), ('Muslim - Others', 'Muslim - Others'), ('Christian', 'Christian'), ('Sikh', 'Sikh'), ('Jain - Digambar', 'Jain - Digambar'), ('Jain - Shwetambar', 'Jain - Shwetambar'), ('Jain - Others', 'Jain - Others'), ('Parsi', 'Parsi'), ('Buddhist', 'Buddhist'), ('Inter-Religion', 'Inter - Religion'), ('Caste No Bar', 'Caste No Bar')], max_length=50, null=True)),
                ('peducation', models.CharField(blank=True, choices=[('99', 'Bachelors - Engineering / Computers / Others'), ('100', 'Masters - Engineering / Computers / Others'), ('101', 'Bachelors - Arts / Science / Commerce / Others'), ('102', 'Masters - Arts / Science / Commerce / Others'), ('103', 'Bachelors - Management / Others '), ('104', 'Masters - Management / Others'), ('105', 'Bachelors - Medicine - General / Dental / Surgeon / Others'), ('106', 'Masters - Medicine - General / Dental / Surgeon / Others'), ('107', 'Bachelors - Legal / Others'), ('108', 'Masters - Legal / Others'), ('109', 'Finance - ICWAI / CA / CS / CFA / Others'), ('110', 'Service - IAS / IPS / IRS / IES / IFS / Others'), ('111', 'PhD'), ('112', 'Diploma / Others'), ('114', 'Higher Secondary / Secondary'), ('215', 'Others')], max_length=50, null=True)),
                ('pcaste', models.CharField(blank=True, max_length=120, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.IntegerField()),
                ('message', models.TextField(null=True)),
                ('user_has_seen', models.BooleanField(default=False)),
                ('recieved_date', models.DateTimeField(auto_now_add=True)),
                ('thread', models.IntegerField(null=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient_notification', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender_notification', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(blank=True, choices=[('4-6', '4ft 6in / 137 cms'), ('4-7', '4ft 7in / 139 cms'), ('4-8', '4ft 8in / 142 cms'), ('4-9', '4ft 9in / 144 cms'), ('4-10', '4ft 10in / 147 cms'), ('4-11', '4ft 11in / 149 cms'), ('5', '5ft / 152 cms'), ('5-1', '5ft 1in / 154 cms'), ('5-2', '5ft 2in / 157 cms'), ('5-3', '5ft 3in / 160 cms'), ('5-4', '5ft 4in / 162 cms'), ('5-5', '5ft 5in / 165 cms'), ('5-6', '5ft 6in / 167 cms'), ('5-7', '5ft 7in / 170 cms'), ('5-8', '5ft 8in / 172 cms'), ('5-9', '5ft 9in / 175 cms'), ('5-10', '5ft 10in / 177cms'), ('5-11', '5ft 11in / 180 cms'), ('6', '6ft / 182 cms'), ('6-1', '6ft 1 in / 185 cms'), ('6-2', '6ft 2in / 187 cms'), ('6-3', '6ft 3in / 190 cms'), ('6-4', '6ft 4in / 193 cms'), ('6-5', '6ft 5in / 195 cms'), ('6-6', '6ft 6in / 198 cms')], max_length=100, null=True)),
                ('familystatus', models.CharField(blank=True, choices=[('Middle Class', 'Middle Class'), ('Upper Middle Class', 'Upper Middle Class'), ('Rich', 'Rich'), ('Elite', 'Elite')], max_length=100, null=True)),
                ('familytype', models.CharField(blank=True, choices=[('Nuclear', 'Nuclear'), ('Joint', 'Joint')], max_length=100, null=True)),
                ('familyvalues', models.CharField(blank=True, choices=[('Orthodox', 'Orthodox'), ('Tradational', 'Tradational'), ('Moderate', 'Moderate'), ('Liberal', 'Liberal')], max_length=100, null=True)),
                ('disability', models.CharField(blank=True, max_length=100, null=True)),
                ('employed', models.CharField(blank=True, choices=[('Self Employed', 'Self Employed'), ('Business', 'Business'), ('Government', 'Government'), ('PSU', 'PSU'), ('MNC', 'MNC'), ('Defence', 'Defence'), ('Private', 'Private'), ('Civil Services', 'Civil Services'), ('Not Working', 'Not Working')], max_length=100, null=True)),
                ('father', models.CharField(blank=True, choices=[('Self Employed', 'Self Employed'), ('Business', 'Business'), ('Government', 'Government'), ('PSU', 'PSU'), ('MNC', 'MNC'), ('Defence', 'Defence'), ('Private', 'Private'), ('Civil Services', 'Civil Services'), ('Not Working', 'Not Working')], max_length=100, null=True)),
                ('mother', models.CharField(blank=True, choices=[('Self Employed', 'Self Employed'), ('Business', 'Business'), ('Government', 'Government'), ('PSU', 'PSU'), ('MNC', 'MNC'), ('Defence', 'Defence'), ('Private', 'Private'), ('Civil Services', 'Civil Services'), ('Not Working', 'Not Working')], max_length=100, null=True)),
                ('brother', models.CharField(blank=True, choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=100, null=True)),
                ('sister', models.CharField(blank=True, choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=100, null=True)),
                ('aboutfamily', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('annualincome', models.CharField(blank=True, choices=[('0', 'Rs. 0 - 1 LAKH'), ('1', 'Rs. 1 - 2 LAKH'), ('2', 'Rs. 2 - 3 LAKH'), ('3', 'Rs. 3 - 4 LAKH'), ('4', 'Rs. 4 - 5 LAKH'), ('5', 'Rs. 5 - 10 LAKH'), ('6', 'Rs. 10 - 20 LAKH'), ('7', 'Rs. 20 - 30 LAKH'), ('8', 'Rs. 30 - 40 LAKH'), ('9', 'Rs. 40 - 50 LAKH'), ('10', 'Rs. 50 - 70 LAKH'), ('11', 'Rs. 70 - 1 Core'), ('12', 'Rs. 1 core & above')], max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('awards', ckeditor.fields.RichTextField(blank=True, null=True)),
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
    ]
