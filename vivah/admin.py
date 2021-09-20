from django.contrib import admin

from vivah.models import Contactme


class ContactmeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')


admin.site.register(Contactme, ContactmeAdmin)
