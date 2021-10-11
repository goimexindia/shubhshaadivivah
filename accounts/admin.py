from django.contrib import admin
from .models import Profile, ColdCoffe, Subscriber, Customer, Preferences

admin.site.register(Profile)
admin.site.register(Subscriber)
admin.site.register(ColdCoffe)
admin.site.register(Customer)
admin.site.register(Preferences)


