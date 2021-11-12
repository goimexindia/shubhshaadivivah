from django import template
from accounts.models import Notification

register = template.Library()


@register.inclusion_tag('accounts/show_notifications.html', takes_context=True)
def show_notifications(context):
    request_user = context['request'].user
    notifications = Notification.objects.filter(recipient=request_user).exclude(user_has_seen=True).order_by('-recieved_date')
    return {'notifications': notifications}
